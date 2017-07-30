function trackingFunction(IdVar, useragentStr,cookieinfo, locationVar,eventtypeStr){
    var dataStr='IdVar='+IdVar+'&useragentStr='+useragentStr+'&cookie='+cookieinfo+'&location='+locationVar+'&event='+eventtypeStr;
    if (IdVar != undefined){
     $.ajax({
        url: '/invokeClick.html?'+dataStr,
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
