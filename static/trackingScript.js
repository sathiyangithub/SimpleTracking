function trackingFunction(Id){
    alert(' Tracking function is invoked ');
    if (Id != undefined){
     $.ajax({
        url: '/invokeClick.html',
        cache: false,
        type: 'POST',
        async: true,
        success: function (data) {
            console.log(data);
        },
        error: function (xhr, ajaxOptions, thrownError) {
            console.log(xhr);
        }
    });
  }
}
