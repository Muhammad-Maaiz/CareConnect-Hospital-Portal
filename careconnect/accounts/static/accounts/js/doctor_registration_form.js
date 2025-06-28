// Image Preview Functionality
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById('imagePreview').style.backgroundImage = 'url(' + e.target.result + ')';
            document.getElementById('imagePreview').innerHTML = '';
        }
        reader.readAsDataURL(input.files[0]);
    }
}

document.getElementById("imageUpload").addEventListener("change", function() {
    readURL(this);
});

// Password Toggle Visibility
const togglePassword = document.querySelector('#togglePassword');
const toggleConfirmPassword = document.querySelector('#toggleConfirmPassword');

togglePassword.addEventListener('click', function() {
    const password = document.querySelector('#password');
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

// Schedule Fields Generation
function showScheduleFields() {
    const selectedDays = document.querySelectorAll('input[name="available_days"]:checked');
    const scheduleContainer = document.getElementById('schedule-fields');
    scheduleContainer.innerHTML = "";

    selectedDays.forEach(day => {
        const dayCode = day.value;
        const dayName = day.dataset.dayName;
        const section = document.createElement('div');
        section.className = 'day-section';

        section.innerHTML = `
            <h4>${dayName}</h4>
            <div class="row">
                <div class="col-md-4 mb-3">
                    <label class="form-label required-field">Start Time</label>
                    <input type="time" class="form-control" name="start_time_${dayCode}" required>
                </div>
                <div class="col-md-4 mb-3">
                    <label class="form-label required-field">End Time</label>
                    <input type="time" class="form-control" name="end_time_${dayCode}" required>
                </div>
                <div class="col-md-4 mb-3">
                    <label class="form-label required-field">Location</label>
                    <input type="text" class="form-control" name="location_${dayCode}" required>
                </div>
            </div>
        `;
        scheduleContainer.appendChild(section);
    });
}