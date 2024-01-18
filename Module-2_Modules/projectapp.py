from projectpkg.auth.signup import signuplib
from projectpkg.auth.login import loginlib
from projectpkg.user import userdata

signuplib.usersignup("Sanket","Chauhan","sanket2020","test@23")

loginlib.userlogin("admin","admin")

userdata.newuser(101,'Sanket','Rajkot')

