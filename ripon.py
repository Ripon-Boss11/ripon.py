<?php

/* SUPER SECRET CHAT SCRIPT

 * Author: Mr. Onion

 * Defult pass is "onio"

 */ 

error_reporting(0);

session_start();

if(! isset($_SESSION["id"])){

	$_SESSION["id"] = bin2hex(substr(md5(uniqid()),0,3));}

// create recent comment

function send_chat($nick,$chat){

	// read/write

	$filename = "chat.json";

	$fopen = fopen($filename,"r");

	$fgets = fgets($fopen);

	fclose($fopen);

	$decode = json_decode($fgets,true);

	// limit 10

	end($decode);

	if(key($decode) >= 10){

		array_shift($decode);

		$new_key = 10;

	}

	else{

		$new_key = key($decode);

		$new_key++;

	}

	$format = array($nick,$chat);

	$decode[$new_key] = $format;

	$encode = json_encode($decode);

	// write

	$fopen_w = fopen($filename,"w");

	fwrite($fopen_w,$encode);

	fclose($fopen_w);

}

function show_chat(){

	$filename = "chat.json";

	$fopen = fopen($filename,"r");

	$fgets = fgets($fopen);

	fclose($fopen);

	$decode = json_decode($fgets,true);

	$val .= "<table class=\"table table-condensed\">";

	foreach($decode as $post){

		$val .= "<tr><td><b style=\"color:#{$post[0]}\">{$post[0]}</b>: {$post[1]}</td></tr>";

	}

	$val .= "</table>";

	return $val;

}

if(isset($_POST["chat"]) && $_POST["chat"] != ""){

	$nick = $_SESSION["id"];

	$chat = $_POST["chat"];

	send_chat($nick,$chat);	

}

if(isset($_GET["chat"]) && $_GET["chat"] != ""){

	echo show_chat();

	exit;

}

?>

<!DOCTYPE html>

<html lang="en">

<head>

  <title>Secret Chat Room</title>

  <meta charset="utf-8">

  <meta name="viewport" content="width=device-width, initial-scale=1">

  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>

  <style>

  #ch{

 visibility: hidden;

 }

 *{margin:0px; 	padding:0px; } 

 

  #password-pro

  {position:absolute; width:100%; height:100%; background:black; margin:auto;} 

  

  input[type=button]

 { 	background:#00aa00; 	padding:8px; 	color:#fff; 	border:1px solid #ccc;

cursor:pointer; 	outline:none; 	font-weight:bold; 	display:block; 	margin:15px auto; 	border-radius:4px; } 

.p_text { color:#fff; 	padding-top:250px; 	font-weight:bold; 	text-align:center; }

.msg{list-style-type:none;}

.msg .nick{text-shadow:1px 2px 3px red;}

  </style>

   <script> 	function passWord() { 	var testV = 1; 	var pass1 = prompt('Please Enter Your Password',' '); 	while (testV < 3) { 	if (!pass1) 	history.go(-1); 	if (pass1.toLowerCase() == "onio") { 	document.getElementById("password-pro").style.display = "none"; 	document.getElementById("ch").style.visibility = "visible";break; 	} 	testV+=1; 	var pass1 = 	prompt('Access Denied - Password Incorrect, Please Try Again.','Password'); 	} 	if (pass1.toLowerCase()!="password" & testV ==3) 	history.go(-1); 	return " "; 	}

   </script>

   <script>

	setInterval(function () { autoloadpage(); }, 2000); // it will call the function autoload() after each 30 seconds. 

	function autoloadpage() {

		$.ajax({

			url: "?chat=1",

			type: "POST",

			success: function(data) {

				$("div#chat").html(data); // here the wrapper is main div

			}

		});

	}

	</script>

  <body>

<section id="lock">

 <div>

 <div id="password-pro" > 	<div class="p_text" > 		You Can't Access This Page Without Password. 		if You Know The Password Please Press "<ter Protected Area</font>" Button. 	</div> 	<input type="button" value="Enter Protected Area" onClick="passWord()"> </div> <!--Main Content--> <div id="pro_hidden">  </div> 

 </div>

 </section>

  <section id="chat">

<div class="container" style="margin-top:5px" id="ch">

<div class="row">

			<div class="col-md-12" id="chat"></div>

			<div class="col-md-12">

				<form id="input-chat" action="" method="post">

					<div class="form-group">

						<label>CHAT...</label>

						<textarea class="form-control" name="chat"></textarea><br>

						<input class="btn btn-sm btn-primary" value="Send" type="submit"/>

						<button type="reset" class="btn btn-sm btn-warning">Refresh</button>

					</div>

				</form>

			</div>

			<div class="col-md-12">

				<p>©: <a href="https://t.me/mronion420" target="_blank">Mr. Onion Telegram</a></p>

			</div>

		</div>

		<script>

		$("#input-chat").submit(function(e)

		{

			var postData = $(this).serializeArray();

			var formURL = $(this).attr("action");

			$.ajax(

			{

				url : formURL,

				type: "POST",

				data : postData,

				success:function(data, textStatus, jqXHR) 

				{

				},

				error: function(jqXHR, textStatus, errorThrown) 

				{

				}

			});

			e.preventDefault();	//STOP default action

		});

			

		$("#input-chat").submit(); //SUBMIT FORM

		</script>

</div>

</section>

 </body>

 </html>
