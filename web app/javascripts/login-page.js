
const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    if (username === "admin" && password === "toor") {
        window.location.href = "/htmls/main.html";
    } else {
        loginErrorMsg.style.opacity = 1;
    }
})