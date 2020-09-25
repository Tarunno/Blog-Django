var author = document.querySelector("#id_author"),
    id = document.querySelector('#author-id').value,
    author_div = document.querySelector('#div_id_author');

author.value = id;
author_div.style.display = 'none';

CKEDITOR.replace( 'post',
{
    width:  '710px',
    height: '200px',
});
