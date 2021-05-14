import tkinter
from tkinter import messagebox

# This code is to hide the main tkinter window
root = tkinter.Tk()
root.withdraw()

# Message Box
messagebox.showinfo("Title", "Message")

<script>
  function login_unsuccessful() {
  if ( {{ login_msg }} == False) {
  alert('Invalid ID or Password')
  }
  }
</script>

@app.route('/loginPublic', methods=['GET', 'POST'])
def login_public():
    login = False
    global nric
    nric = None
    create_user_form = LoginPublicForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        users_dict = {}
        db = shelve.open('public_storage.db', 'r')
        users_dict = db['Users']
        db.close()
        nric = create_user_form.nric.data
        hashing = hashlib.md5(create_user_form.password.data.encode())
        password = hashing.hexdigest()

        if nric in users_dict:
            user = users_dict[nric]
            correct_password = user.get_password()
            print(correct_password)
            print(password)
            if correct_password == password:
                print('Login successful')
                print(correct_password)
                login = True
                return render_template('homePublic.html', login_msg = login_unsuccessful(login))
            else:
                print('Invalid ID or Password!')
        else:
            print('Invalid ID or Password!')
    return render_template('loginPublic.html', form=create_user_form, login_msg = login_unsuccessful(login), login = login)
