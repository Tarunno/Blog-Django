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
    if(window.innerWidth > 1300){
        e.target.style.left = '81%';
    }
    else if(window.innerWidth >= 1200 && window.innerWidth <= 1300){
        e.target.style.left = '80%';
    }
    else if(window.innerWidth >= 1100 && window.innerWidth <= 1199){
        e.target.style.left = '78%';
    }
    else if(window.innerWidth >= 1000 && window.innerWidth <= 1099){
        e.target.style.left = '76%';
    }
    else if(window.innerWidth >= 900 && window.innerWidth <= 999){
        e.target.style.left = '75%';
    }
    else{
        e.target.style.left = '74%';
    }
}
function close(e){
    e.target.style.transition = '.5s';
    if(window.innerWidth > 1300){
        e.target.style.left = '97%';
    }
    else if(window.innerWidth >= 1200 && window.innerWidth <= 1300){
        e.target.style.left = '96.5%';
    }
    else if(window.innerWidth >= 1100 && window.innerWidth <= 1199){
        e.target.style.left = '96.5%';
    }
    else if(window.innerWidth >= 1000 && window.innerWidth <= 1099){
        e.target.style.left = '96%';
    }
    else if(window.innerWidth >= 900 && window.innerWidth <= 999){
        e.target.style.left = '95.5%';
    }
    else{
        e.target.style.left = '95%';
    }
}

//Alert
var link_btn = document.querySelectorAll('#read-post-alert-like');
var comment_btn = document.querySelectorAll('#read-post-alert-comment');

link_btn.forEach((item) => {
    item.addEventListener('click', check);
});
comment_btn.forEach((item) => {
    item.addEventListener('click', check);
});

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
        <button class="alert-cnl-btn"> <i class="fas fa-times"></i> </button>
        <h1> Read the post first! </h1>
       <a href="single/${id}" class="alert-login-btn"> Read </a>
    `;
    body.appendChild(Alert_container);
    body.appendChild(Alert_window);
    document.querySelector('.alert-cnl-btn').addEventListener('click', function(){
        body.removeChild(Alert_window);
        body.removeChild(Alert_container);
    });
}
