document.getElementById('employeeBtn').addEventListener('click', function() {
    this.classList.add('active');
    document.getElementById('adminBtn').classList.remove('active');
});

document.getElementById('adminBtn').addEventListener('click', function() {
    this.classList.add('active');
    document.getElementById('employeeBtn').classList.remove('active');
});

let isSignUp = false;
const authForm = document.getElementById('authForm');
const toggleButton = document.getElementById('toggleButton');
const toggleText = document.getElementById('toggleText');

function toggleForm() {
    isSignUp = !isSignUp;
    authForm.innerHTML = isSignUp ? `
        <label for="username">Username</label>
        <input type="text" id="username" placeholder="Username" required>
        <label for="email">Email</label>
        <input type="email" id="email" placeholder="Email" required>
        <label for="password">Password</label>
        <input type="password" id="password" placeholder="Password" required>
        <button type="submit">Sign Up</button>
    ` : `
        <label for="email">Email</label>
        <input type="email" id="email" placeholder="Email" required>
        <label for="password">Password</label>
        <input type="password" id="password" placeholder="Password" required>
        <div class="options">
            <label>
                <input type="checkbox"> Remember me
            </label>
            <a href="#">Forgot Password?</a>
        </div>
        <button type="submit">Sign In</button>
    `;
    toggleText.innerHTML = isSignUp ? 'Already have an account? <a href="#" id="toggleButton">Sign In</a>' : "Don't have an account? <a href='#' id='toggleButton'>Sign Up</a>";
    document.getElementById('toggleButton').addEventListener('click', toggleForm);
}

document.getElementById('toggleButton').addEventListener('click', toggleForm);

authForm.addEventListener('submit', function(event) {
    event.preventDefault();
    // Perform authentication logic here
    // If authentication is successful, redirect to the home page
    window.location.href = 'home.html';
});