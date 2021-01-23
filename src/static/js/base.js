$(document).ready(function(){
    $("#page-select").val(Cookies.get('items_on_page'));
})

function setItemsOnPage(element) {
    Cookies.set('items_on_page', element.value);
    document.location.reload();
}
