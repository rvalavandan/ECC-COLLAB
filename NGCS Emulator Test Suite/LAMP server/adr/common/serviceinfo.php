<?php

header('Connection: close');
header('Content-Type: application/emergencycalldata.serviceinfo+xml; charset=utf-8');

// header('Transfer-Encoding: chunked');

$tn = $_GET['tn'];


function gen_uuid() {
    return sprintf( '%04x%04x-%04x-%04x-%04x-%04x%04x%04x',
        // 32 bits for "time_low"
        mt_rand( 0, 0xffff ), mt_rand( 0, 0xffff ),

        // 16 bits for "time_mid"
        mt_rand( 0, 0xffff ),

        // 16 bits for "time_hi_and_version",
        // four most significant bits holds version number 4
        mt_rand( 0, 0x0fff ) | 0x4000,

        // 16 bits, 8 bits for "clk_seq_hi_res",
        // 8 bits for "clk_seq_low",
        // two most significant bits holds zero and one for variant DCE1.1
        mt_rand( 0, 0x3fff ) | 0x8000,

        // 48 bits for "node"
        mt_rand( 0, 0xffff ), mt_rand( 0, 0xffff ), mt_rand( 0, 0xffff )
    );
}


$servername = "localhost";
$username = "emulator";
$password = "#87679TheSilenceoftheLambs98938#";
$dbname = "dbsEmulator";

// Create connection
$conn = new mysqli($servername, $username, $password,$dbname);

//$tn = "14038748354";

$query = "SELECT service_type,service_mobility,service_environment,provider_reference from call_data where telephone_number =  '$tn';";


$result = $conn->query($query);

if ($result->num_rows > 0) {
  while($row = $result->fetch_assoc()) {
    $dataProviderReference = $row["provider_reference"];
        $serviceMobility= $row["service_mobility"];
        $serviceType= $row["service_type"];
        $serviceEnvironment= $row["service_environment"];

  }
} else {
  echo "0 results";
}



// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}


$conn->close();



$doc = new DOMDocument('1.0', 'utf-8');
$root = $doc->createElement('EmergencyCallData.ServiceInfo');
$root->setAttribute('xmlns', 'urn:ietf:params:xml:ns:EmergencyCallData:ServiceInfo');
$doc->appendChild($root);


$dataProviderRefElement = $doc->createElement('DataProviderReference', $dataProviderReference);
$root->appendChild($dataProviderRefElement);

$serviceEnvironmentElement = $doc->createElement('ServiceEnvironment', $serviceEnvironment);
$root->appendChild($serviceEnvironmentElement);

$serviceTypeElement = $doc->createElement('ServiceType', $serviceType);
$root->appendChild($serviceTypeElement);

$serviceMobilityElement = $doc->createElement('ServiceMobility', $serviceMobility);
$root->appendChild($serviceMobilityElement);

$doc->formatOutput = true;

echo $doc->saveXML();

?>