jQuery(document).ready(function($) { 
    $(".scroll").click(function(event){		
	event.preventDefault();
	$('html,body').animate({scrollTop:$(this.hash).offset().top}, 500);
     });
    $('body').hide();
    $(window).load(function(){
        $('body').show();
    });
});
