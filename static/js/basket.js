window.onload = function () {
    $( '.basket_list' ).on( 'click' , 'input[type="number"]' , function () {
        let t_href = event.target;
        $.ajax({url: `/edit/${t_href.name}/?quantity=${t_href.value}`});
        event.preventDefault();
    });
};

