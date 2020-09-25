category_list();


function category_list(){
    var tab = document.querySelector('.category-list'),
        heading = document.querySelector('.category-list h1'),
        list = document.querySelector('.category-list ul');

    tab.addEventListener('mouseenter', open);
    tab.addEventListener('mouseleave', close);

}
function open(e){
    e.target.style.transition = '.5s';
    e.target.style.left = '76vw';
}
function close(e){
    e.target.style.transition = '.5s';
    e.target.style.left = '95vw';
}

//Alert
document.querySelector('#read-post-alert-like').addEventListener('click', check);
document.querySelector('#read-post-alert-comment').addEventListener('click', check);

function check(e){
    var post_id = e.target.parentNode.getAttribute('post_id');
    Alert(post_id);
}

function Alert(id){
    var body = document.body,
        Alert_container = document.createElement('div'),
        Alert_window = document.createElement('div');

    Alert_container.setAttribute('class', 'alert-container');
    Alert_window.setAttribute('class', 'alert-window');
    Alert_window.innerHTML = `
        <button class="alert-cnl-btn"> <i class="far fa-times-circle"></i> </button>
        <h1> Read the post first! </h1>
       <a href="../../single/${id}" class="alert-login-btn"> Read </a>
    `;
    body.appendChild(Alert_container);
    body.appendChild(Alert_window);
    document.querySelector('.alert-cnl-btn').addEventListener('click', function(){
        body.removeChild(Alert_window);
        body.removeChild(Alert_container);
    });
}