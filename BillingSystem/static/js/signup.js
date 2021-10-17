var lengthOfPasswordError = document.getElementById("invalidPassword");
var matchPassword = document.getElementById("matchPassword");

function lengthOfPassword(){
		var length = document.getElementById("inputPassword4").value.length;

		if(length < 8)
            lengthOfPasswordError.innerHTML = "password should be minimum of 8 char";

        else if (length > 12)
            lengthOfPasswordError.innerHTML = "password should not be more than of 12 char";
        else
            lengthOfPasswordError.innerHTML = "";
}

function matchPassword(){
    var confirmPassword = document.getElementById("inputConfirmPassword4");
    var password = document.getElementById("inputPassword4");
    alert("okk");
    if(password.value != confirmPassword.value){
        matchPassword.innerHTML = "Password is not matching"
    }
    else
    matchPassword.innerHTML = ""
}