/**
 * Send the contact message
 */
function sendContact() {
    $("#btn-contact-send").click(function() {
        // validate

        // send
        var url = "/contato/enviar";
        $.ajax({
            type: 'POST',
            url: url,
            data: $("#form-contact").serialize(),
            success: function(data) {
                if (data.result == 'success') {
                    console.debug("success - " + data.message);
                } else if (data.result == 'fail') {
                    console.debug("fail - " + data.message);
                } else {
                    console.debug("fail");
                }
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                console.debug(XMLHttpRequest);
                console.debug(textStatus);
                console.debug(errorThrown);
            },
            dataType: 'json'
        });
    });
}

/**
 * On load.
 */
$(document).ready(function() {
    sendContact();
});

