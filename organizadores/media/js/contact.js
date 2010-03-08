/**
 * Send the contact message
 */
function sendContact() {
    $("#btn-contact-send").click(function() {
        var $message = $("#message");
        $message.removeClass("contact-message-fail")
        $message.removeClass("contact-message-success")
        $message.hide();

        var validationMessage = "Favor preencher todos os campos para o envio do contato.";
        var errorMessage = "Erro ao enviar a mensagem. Por favor tente mais tarde ou se preferir envie um e-mail direto para contato@organizadores.com.br."

        // validate
        var name = $("input#name").val();
        var email = $("input#email").val();
        var message = $("input#message").val();

        if (name == '' || email == '' || message == '') {
            $message.addClass("contact-message-fail").text(validationMessage).fadeIn();
            return;
        }

        // loading
        var $form = $("#form").hide();
        var $loader = $("#loader").addClass("loading").fadeIn();

        // send
        var url = "/contato/enviar";
        $.ajax({
            type: 'POST',
            url: url,
            data: $("#form-contact").serialize(),
            success: function(data) {
                $loader.hide();
                if (data.result == 'success') {
                    $message.addClass("contact-message-success").text(data.message).fadeIn();
                } else if (data.result == 'fail') {
                    $form.fadeIn();
                    $message.addClass("contact-message-fail").text(data.message).fadeIn();
                } else {
                    $form.fadeIn();
                    $message.addClass("contact-message-fail").text(errorMessage).fadeIn();
                }
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                $loader.hide();
                $form.fadeIn();
                $message.addClass("contact-message-fail").text(errorMessage).fadeIn();
                //console.debug(textStatus);
                //console.debug(errorThrown);
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
    // adjusting the height
    $("#content").height(450);
});

