function viewProduct(id) {
    var url = "/products/" + id + "/";
    $.get(url, function(data) {
        var $popin = $("#popin-dialog-modal");
        var product = data[0].fields;
        $popin.dialog({
            width: 600,
			height: 450,
			modal: true,
            title: product.name
		});
        $popin.find("p").text(product.full_description);
        /*
        $highlightVertical.find("#highlight-title").text(item.fields.title);
        $highlightVertical.find("#highlight-link").attr("href", item.fields.link);
        $highlightVertical.find("#highlight-image").attr("src", "/media/" + item.fields.photo);
        $highlightVertical.find("#highlight-content").text(item.fields.content);
        */
    });

}
