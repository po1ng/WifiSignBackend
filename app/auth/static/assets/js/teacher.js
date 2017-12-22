var data1;
var data2;
var object_js;
var s=new Array();
s.push('btn-danger');
s.push('btn-success');
var messageList=document.getElementById('message-list');
var allListadmin=document.getElementById('all-list-admin');
var object_no;
var noList=document.getElementById('no-list');
var student_name;
class_number=1718011;
function changeClass(which){
if(which!=null){
	class_number = $(which).text();
	$("#classList").show();
	$("#clone").css("display","none");
	var span=document.getElementById("class");
	span.innerHTML = class_number;
 }
	$.ajax({
		url: 'http://119.29.184.156:9000/admin/student_connect_status/data', //在这里提填写你的地址
		async: false,
		dataType: 'jsonp',
		data:{'class_number':class_number},
		type:'get',
		jsonp:"callback_admin", 
		crossDomain: true,
		jsonpCallback:"callback_admin",
		success: function (json_str) {
			object_js = json_str;
			showAllListadmin();
		}
	});
}

function showAllListadmin(){
	$('#all-list-admin tr').remove();
	var size=0,key;
	var statuses=new Array();
	var names=new Array();
	for(key in object_js){
		if(object_js.hasOwnProperty(key)){
			names.push(key);
			statuses.push(object_js[key]);
			size++;
		}
	}
	
	var i=0;
	for(i=0;i<size;){
		var tr=document.createElement('tr');
		do{
			if(i>=size){
				break;
			}
			var td=document.createElement('td');
			var btn=document.createElement('a');
			btn.innerHTML=names[i];
			btn.setAttribute('onclick','student_message(this)');
			$(btn).attr('href','#');
			$(btn).addClass('btn');
			$(btn).css('width','100%');
			$(td).css('width','14.2%');
			$(btn).addClass(s[statuses[i]]);
			td.appendChild(btn);
			tr.appendChild(td);
			i++;
		}while(i%7!=0);
		allListadmin.appendChild(tr);
	}
}
function student_message(which){

student_name=which.innerHTML;
$("#classList").hide();
$("#clone").css("display","");
changeMessage();
}

function changeMessage(){
	$.ajax({
		url: 'http://119.29.184.156:9000/admin/list', //在这里提填写你的地址
		async: false,
		dataType: 'jsonp',
		data:{'student_name':student_name},
		type:'get',
		jsonp:"callback_info", 
		crossDomain: true,
		jsonpCallback:"callback_info",
		success: function (json_str) {
			object_js = json_str;
			showMessageList();
		}
	});
}
function createInfo(text,tr){
	var td=document.createElement('td');
	var btn=document.createElement('a');
	$(td).css("padding","0px");
	$(td).css("margin-top","0px");
	btn.innerHTML=text;
	$(btn).attr('href','#');
	$(btn).addClass('btn');
	$(td).css('width','12.5%');
	$(btn).css('width','100%');
	$(btn).css('height','100%');
	$(btn).css('background','white');
	$(btn).css('color','black');
	$(btn).css('border','1px solid black');
	$(btn).css('border-radius','0');
	var maxNum=$(btn).html();
		if(maxNum.length>25){
			$(btn).html(maxNum.substr(0,25)+"...")
	}
	btn.setAttribute('title',text);
	td.appendChild(btn);
	tr.appendChild(td);
	messageList.appendChild(tr);
}

function showMessageList(){
	$('#message-list tr').remove();
	var students_list = object_js.list;
	for(var i = 0; i < students_list.length; i++){
		student = students_list[i];
		var info_list = new Array();
		var tr=document.createElement('tr');
		var name = student['name'];
		var student_id = student['student_id'];
		var class_id = student['class_id'];
		var address_mac = student['address_mac'];
		var connect_time = student['connect_time'];
		var break_time = student['break_time'];
		var student_status = student['status'];
        var date = student['date']
		var remarks = student['remarks'];
		createInfo(name, tr);
		createInfo(student_id, tr);
		createInfo(class_id, tr);
		createInfo(address_mac, tr);
		createInfo(connect_time, tr);
		createInfo(break_time, tr);
		createInfo(date, tr);
		createInfo(remarks, tr);
		messageList.appendChild(tr);
	}
}

window.onload=function(){
	changeClass();
	data2=setInterval('changeClass()',2000);//6000是间隔时间  单位为毫秒 6000就是一分钟
} 
