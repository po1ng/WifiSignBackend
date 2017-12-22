$(document).ready(function() {
    var temp = "none";

    $("#li-one").click(function () {
        openMatter(1);
    });
    $("#li-two").click(function () {
        openMatter(2);
    });
    $("#li-three").click(function () {
        openMatter(3);
    });
    $("#li-four").click(function () {
        openMatter(4);
    });
    $("#li-five").click(function () {
        openMatter(5);
    });
    $("#li-six").click(function () {
        openMatter(6);
    });
    $("#li-seven").click(function () {
        openMatter(7);
    });
    $("#li-eight").click(function () {
        openMatter(8);
    });
    $("#li-nine").click(function () {
        openMatter(9);
    });
	$("#li-ten").click(function () {
		upDate();
        openMatter(10);
    });
   
    function openMatter(obj) {
        for (var i = 1; i < 11; i++) {
            if (i == obj) {
                temp = "block";
            } else {
                temp = "none";
            }
            document.getElementById("matter" + i).style.display = temp;

        }
    }
});
function upDate(){
	
	$.ajax({
		url: 'http://119.29.184.156:9000/auth/reflash', //在这里提填写你的地址
		async: false,
		dataType: 'jsonp',
		data:{'upDate':"success"},
		type:'get',
		jsonp:"callback_upDate", 
		crossDomain: true,
		jsonpCallback:"callback_upDate",
		success: function (json_str) {
			
		}
	});
}

	
