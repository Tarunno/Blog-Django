// Comment
var post_id = document.querySelector('.post_id').value,
    commenter_id = document.querySelector('.user_id').value,
    post_id_field = document.querySelector('#id_post'),
    commenter_field = document.querySelector('#id_user');

post_id_field.value = post_id;
commenter_field.value = commenter_id;

post_id_field.style.display = 'none';
commenter_field.style.display = 'none';

// login alert
document.querySelector('#login-message').addEventListener('click', Alert);
document.querySelector('#comment-login-alert').addEventListener('click', Alert);

function Alert(){
    var body = document.body,
        Alert_container = document.createElement('div'),
        Alert_window = document.createElement('div');

    Alert_container.setAttribute('class', 'alert-container');
    Alert_window.setAttribute('class', 'alert-window');
    Alert_window.innerHTML = `
        <button class="alert-cnl-btn"> <i class="fas fa-times"></i> </button>
        <h1> Login please! </h1>
        <a href="/login/" class="alert-login-btn"> Login </a>
    `;
    body.appendChild(Alert_container);
    body.appendChild(Alert_window);
    document.querySelector('.alert-cnl-btn').addEventListener('click', function(){
        body.removeChild(Alert_window);
        body.removeChild(Alert_container);
    });
}
