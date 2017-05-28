window.onload = function () {
	document.getElementById("source-code").oninput = validatePassword;
}

function validatePassword(){
	var maxLines = 5;
	var maxChars = 50;

	var submit = document.getElementById("submit");
  var content = document.getElementById("source-code").value.trim();
  var nbLines = content.split(/\r\n|\r|\n/).length;
	var nbChars = content.length;

  if (nbLines >= maxLines || nbChars >= maxChars) {
		submit.removeAttribute("disabled");
		submit.value = "Guess now!";
	} else {
		submit.setAttribute("disabled", "disabled");
		submit.value = (
			"Please paste more code: -" + (maxLines - nbLines) +
			" lines, -" + (maxChars - nbChars) + " chars"
		);
	}
}
