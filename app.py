from flask import Flask,render_template,request,redirect,url_for
from flask_mail import Mail, Message
from datetime import date,datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import delete
import random 
app = Flask(__name__)
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/urban_inovations'
# # initialize the app with the extension
db.init_app(app)
 
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'urbaninnovationss@gmail.com'
app.config['MAIL_PASSWORD'] = 'password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

 
def randomm():
     return str(random.randrange(0,9))
def transaction_gen():
     trans=""
     for i in range(12):
          trans+=randomm()
     pre_trans=Payment_details.query.with_entities(Payment_details.transaction_id).all()   
     if(trans!=pre_trans):
          return trans
     else:
          transaction_gen()   
@app.route('/')
def hello_world():
    s=1
    return render_template('index.html')

 
class Login(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
class Account_details(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)  
    phone_no = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
class Booking_details(db.Model):
    count=db.Column(db.Integer,primary_key=True)
    sno = db.Column(db.Integer )
    cost = db.Column(db.Integer, nullable=False)
    transaction_id = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    date_of_booking = db.Column(db.DateTime, nullable=False)
    type = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
class Payment_details(db.Model):
    count=db.Column(db.Integer,primary_key=True)
    sno = db.Column(db.Integer)
    cvv = db.Column(db.Integer, nullable=False)
    card_number = db.Column(db.String(255), nullable=False)
    card_holder = db.Column(db.String(255), nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    transaction_id = db.Column(db.String(255), nullable=False)
    expiry_date = db.Column(db.String(255), nullable=False)
costt={'Kitchen':10000,'Living Room':30000,'Washroom':35000,'Bedroom':50000}
ss={} 
lss={}
lis={}
@app.route('/user')
def user_dashbaord():
    user_booking=Booking_details.query.filter_by(sno=ss['sno']).all()
    user_payment=Payment_details.query.filter_by(sno=ss['sno']).all()
    print(user_booking,user_payment)
    for h in user_booking:
         print(h.name)
    for j in user_payment:
         print(j.card_number)
    return render_template('user_dashboard.html',user_booking=user_booking,user_payment=user_payment)

@app.route('/delete',methods=['GET','POST'])
def delete():
    
    if request.method == 'POST':
        transaction_id=request.form.get('transaction_id')
        print("mother",transaction_id)
        obj = Booking_details.query.filter_by(transaction_id =transaction_id).one()
        db.session.delete(obj)
        db.session.commit()
        msg = Message(subject='Cancellation mail!', sender='urbaninnovationss@gmail.com', recipients=[obj.email])
        msg.body = "Hey {0} ,Your Booking  on date :{1} is CANCELLED\n Your amount will be refunded \n More details are \n booking name:{2}\n type:{3}\n \n this is a auto generated message".format(obj.name,obj.date_of_booking,obj.name,obj.type)
        mail.send(msg)
        # Execute the delete query
        
        
         
        # Booking_details.query.filter(transaction_id == transaction_id).delete()
        # db.session.execute("delete from booking_details where transaction_id = {0}".format(transaction_id))
         
    return redirect(url_for('user_dashbaord'))

@app.route('/login/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        type = request.form.get('type')
        booking_date = request.form.get('booking_date')
         
        lss['name']=name
        lss['email']=email
        lss['type']=type
        lss['booking_date']=booking_date

        global lis
        sno = Login.query.filter(Login.email == email).first()
        snoo = sno.sno 
        lis['sno']=snoo
        lis['name']=name
         
        
        return redirect(url_for('payment'))
    
    return render_template('booking.html')
details={}
 

@app.route('/login/payment', methods=['GET', 'POST'])
def payment():
    print(lss)
    typee=lss['type']
    print(typee)
    cost=costt[typee]
    print(cost)
    if request.method == 'POST':   
        global lis
        card_number = request.form.get('card_number')
        exp_date = request.form.get('expiry_date')
        cvv = request.form.get('cvv')
        card_holder = request.form.get('card_holder')
        transaction=transaction_gen()
        rec = Payment_details(sno=lis['sno'], card_number=card_number, expiry_date=exp_date, cvv=cvv, card_holder=card_holder, transaction_id=transaction, cost=cost)
        db.session.add(rec)
        db.session.commit()
        rec = Booking_details(sno=lis['sno'], name=lss['name'], email=lss['email'], type=lss['type'], date_of_booking=lss['booking_date'],cost=cost,transaction_id=transaction)
        db.session.add(rec)
        db.session.commit()
        namee=lss['name']
        msg = Message(subject='Booking Confirmation mail!', sender='urbaninnovationss@gmail.com', recipients=[lss['email']])
        msg.body = "Hey {0} ,Your Booking is confirmed on date :{1}\n More details are \n booking name:{2}\n type:{5}\n cost:{3} \n transaction id:{4}\n this is a auto generated message".format(namee,lss['booking_date'],namee,cost,transaction,lss['type'])
        mail.send(msg)
        return f'Payment successful for {namee}'
    
    return render_template('payment.html',cost=costt[typee])
opt={}
strr={}



@app.route('/opts',methods=['POST'])
def opt():
     opt=request.form.get('opt')
     print("form opt",opt)
     if request.method == 'POST':    
         
        current_date_time = datetime.utcnow()
        formatted_date_time = current_date_time.strftime('%Y-%m-%d %H:%M:%S')
        ent =Account_details(name=details['name'], phone_no = details['phone'],address=details['address'],email=details['email'],date=formatted_date_time )
        print(formatted_date_time)
        print("dict opt",strr['opt'])
        if(strr['opt']==opt):
                    
                    namee=details['name']
                    loggin=Login(email=details['email'],password=details['pass'])
                    db.session.add(loggin)
                    db.session.add(ent)
                    db.session.commit()
                    return f'account created {namee}'  
        else:
                    return f'invalid otp'
     return render_template('opt.html')      

     
      
def hashing(passsworrrd):
        passsworrrd=list(passsworrrd)
        lst=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z','1','2','3','4','5','6','7','8','9','0','#','%','@','&','*','!','a','b','c','s','d','e','$','v','f','f','5','4','4','d','f','5']
        word1=''
        for i in passsworrrd:
            if i in lst:
                worrd=lst.index(i)
                final=lst[abs(worrd+3)]+lst[abs(worrd+9)]+lst[abs(worrd+10)]+lst[abs(worrd+12)]
                word1+=final
        return word1
 
@app.route('/login',methods=['GET','POST'])
def login():
    s=0
    
    email=request.form.get('email')
    password=request.form.get('password')
    if request.method == 'POST':     
        user = Login.query.filter_by(email=email, password=hashing(password)).first()
        if((email=="urban_inovation@gmail.com" and password=='vinay') ):
                s=1
                booking_detail=Booking_details.query.all()
                payment_detail=Payment_details.query.with_entities(Payment_details.cost).all()
                costt=0
                for j in payment_detail:
                     costt+=int(j.cost)
                payment_details_All=Payment_details.query.all()
                return render_template('admin_dashboard.html',booking_detail=booking_detail,totals=len(booking_detail),costt=costt,payment_details_All=payment_details_All)
           
        elif(user!=None): 
             sno = Login.query.filter(Login.email == email).first().sno
             print("fuck",sno)
             ss['sno']=sno
             return user_dashbaord()
            
        else:
             s=2           
    return render_template('index.html',s=s,data=user)
 
@app.route('/enntry',methods=['POST'])
def entry():
    if request.method == 'POST':    
        name=request.form.get('username')
        phone_number=request.form.get('phone_number')
        email=request.form.get('email')
        address=request.form.get('address')
        password=request.form.get('password')
        confirm=request.form.get('confirmpassword')
        details['name']=name
        details['phone']=phone_number
        details['address']=address
        details['email']=email
        
         
        if(password==confirm):
            otp=randomm()+randomm()+randomm()+randomm()
            strr['opt']=otp
            msg = Message(subject='OTP', sender='urbaninnovationss@gmail.com', recipients=[email])
            msg.body = "Your OTP is :{0}".format(otp)
            mail.send(msg)
            print('before hashoinh:',password)
            details['pass']=hashing(password)
            print('password after hashing in dict:',details['pass'])
             
            return render_template('opt.html')
             
             
        else:
              return render_template('registration-form.html',password=password,confirm=confirm) 
    
@app.route('/registration-form')
def registration_form():
    return render_template('registration-form.html')

if __name__=="__main__":
    app.run(debug=True)