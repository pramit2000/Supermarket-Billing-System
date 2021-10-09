var lengthOfPasswordError = document.getElementById("invalidPassword");

function lengthOfPassword(){

		var length = document.getElementById("inputPassword4").value.length;

		if(length < 8)
            lengthOfPasswordError.innerHTML = "     password should be minimum of 8 char";

        else if (length > 12)
            lengthOfPasswordError.innerHTML = "     password should not be more than of 12 char";
        else
            lengthOfPasswordError.innerHTML = "";
	}

function matchPassword(){

}