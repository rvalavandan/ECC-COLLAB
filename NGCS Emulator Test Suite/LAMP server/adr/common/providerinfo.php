<?php

header('Connection: close');
header('Content-Type: application/emergencycalldata.providerinfo+xml; charset=utf-8');

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

$query = "SELECT provider_id,provider_contact_number,provider_string,provider_reference from call_data where telephone_number =  '$tn';";


$result = $conn->query($query);

if ($result->num_rows > 0) {
  while($row = $result->fetch_assoc()) {
    $dataProviderReference = $row["provider_reference"];
        $contactUri = 'tel:'.$row["provider_contact_number"];
        $dataProviderString = $row["provider_string"];
        $providerId = 'urn:nena:companyid:'.$row["provider_id"];

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
$root = $doc->createElement('EmergencyCallData.ProviderInfo');
$root->setAttribute('xmlns', 'urn:ietf:params:xml:ns:EmergencyCallData:ProviderInfo');
$doc->appendChild($root);

$dataProviderRefElement = $doc->createElement('DataProviderReference', $dataProviderReference);
$root->appendChild($dataProviderRefElement);

// DataProviderString
$dataProviderStringElement = $doc->createElement('DataProviderString', $dataProviderString);
$root->appendChild($dataProviderStringElement);

// ProviderID
$providerIdElement = $doc->createElement('ProviderID', $providerId);
$root->appendChild($providerIdElement);

// ProviderIDSeries
$providerIdSeriesElement = $doc->createElement('ProviderIDSeries', 'NENA');
$root->appendChild($providerIdSeriesElement);

// TypeOfProvider
$typeOfProviderElement = $doc->createElement('TypeOfProvider', 'Telecom Provider');
$root->appendChild($typeOfProviderElement);

// ContactURI
$contactUriElement = $doc->createElement('ContactURI', $contactUri);
$root->appendChild($contactUriElement);

// Language
$languageElement = $doc->createElement('Language', 'en');
$root->appendChild($languageElement);

// Format the XML to be readable (Optional but recommended)
$doc->formatOutput = true;

// Output
echo $doc->saveXML();

?>
