$('#file').on('change',function(){
    var fileName = this.files[0].name
    $('.imgPic').text(fileName);
});