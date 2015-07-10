

function checkUserEmail() {
    $.get("my_auth/check_email/", 
        {user_mail: $("#user_mail").val()},
        function(data) {
            if ( data == 'True' ) {
                $("#mail_img").html("<img src='/static/img/ok.png'>");
                $("#mail_status").val('');
            } else {
                $("#mail_img").html("<img src='/static/img/no.png'>");
                $("#mail_status").val('0');
            }
        }
    );
}

function validateMailStr() {
    var LIVR = require('https://github.com/koorchik/js-validator-livr/blob/master/dist/livr-debug.js');
    LIVR.Validator.defaultAutoTrim(true);

    var validator = new LIVR.Validator({
        user_mail: 'email'
    });
    var chackedData = validator.validate({
        user_mail: $("#user_mail").val()
    });
    $('#error').html("Wrong email format"+ chackedData +"!")
    return false;
}

function validateForm() {
    var userMail = $("#user_mail").val() == "";
    var userName = $("#username").val() == "";
    var password = $("#password").val() == "";
    var confirmPassword = $("#confirmp_assword").val() == "";

    if ( userMail || userName || password || confirmPassword ) {
        $('#error').html("fill required field!");
        return false;
    };

    if ( $("#mail_status").val() == '0') {
        $('#error').html("User with this email alredy exist!");
        return false;
    };

    if ( $("#password").val() != $("#confirmp_assword").val() ) {
        $('#error').html("You not confirm a password!");
        return false;
    };
    return true;
}

$(document).ready(function() { 
    $('#user_mail').keyup(checkUserEmail); 
});