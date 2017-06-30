<?php
header('Access-Control-Allow-Origin: *');
	
$remetente = $_POST['nome'] . " <" . $_POST['email'] . ">";
$nome = $_POST['nome'];
$msg = $_POST['mensagem'];
 
$destino = "matwebaed@outlook.com"; // o email que irá receber os emails do site
 
$html_msg = "
            <html>
                <head>
                    <title>Contato - Site</title>
                    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">
                </head>
                <body>
                    <font size=\"1\" face=\"verdana\">
                        <strong>EmpresaSA (Contato pelo Site)</strong>
                    </font>
                    <font face=\"verdana\">
                        <p>
                            <font size=\"1\">
                                <strong>Nome:</strong>  $nome <br>
                                <strong>Mensagem:</strong> $msg 
                            </font>
                        </p>
                    </font>
                </body>
            </html>
            "; //MENSAGEM NO FORMATO HTML
                
$headers  = "MIME-Version: 1.0\r\n";
$headers .= "Content-type: text/html; charset=utf-8\r\n";
$headers .= "From: ". $remetente ."\r\n";
$headers .= "Reply-To: ". $remetente ."\r\n";
$headers .= "X-Priority: 1\r\n";
$headers .= "X-MSMail-Priority: High\r\n";
$headers .= "X-Mailer: Just My Server";
    
    
if (imap_mail($destino, $assunto, ($html_msg), $headers)) {
    $data = array('enviado' => true );
    echo json_encode($data);
}else{
 	$data = array('enviado' => false);
    echo json_encode($data);
}