function exibirSenha() {
    var passwordInput = document.getElementById("senha");
    var passwordToggleIcon = document.getElementById("password-toggle-icon");
  
    if (passwordInput.type === "password") {
      passwordInput.type = "text";
      passwordToggleIcon.classList.remove("fa-eye");
      passwordToggleIcon.classList.add("fa-eye-slash");
    } else {
      passwordInput.type = "password";
      passwordToggleIcon.classList.remove("fa-eye-slash");
      passwordToggleIcon.classList.add("fa-eye");
    }
  }

  
  