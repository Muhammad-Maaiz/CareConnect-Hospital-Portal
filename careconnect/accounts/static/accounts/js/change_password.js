// Password Toggle Visibility
const toggleNewPassword = document.querySelector('#toggleNewPassword');
const toggleConfirmPassword = document.querySelector('#toggleConfirmPassword');

toggleNewPassword.addEventListener('click', function() {
    const password = document.querySelector('#new_password');
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
    
    const icon = this.querySelector('i');
    icon.classList.toggle('fa-eye');
    icon.classList.toggle('fa-eye-slash');
});

toggleConfirmPassword.addEventListener('click', function() {
    const confirmPassword = document.querySelector('#confirm_password');
    const type = confirmPassword.getAttribute('type') === 'password' ? 'text' : 'password';
    confirmPassword.setAttribute('type', type);
    
    const icon = this.querySelector('i');
    icon.classList.toggle('fa-eye');
    icon.classList.toggle('fa-eye-slash');
});