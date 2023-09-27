<?php

header('Connection: close');
header('Content-Type: application/EmergencyCallData.SubscriberInfo+xml; charset=utf-8');

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

$query = "SELECT A3,A1,PC,country,NAM,street_address,telephone_number,provider_reference from call_data where telephone_number =  '$tn';";


$result = $conn->query($query);

if ($result->num_rows > 0) {
  while($row = $result->fetch_assoc()) {
    $dataProviderReference = $row["provider_reference"];
        $locality = $row["A3"];
        $street_address = $row["street_address"];
        $region = $row["A1"];
        $code = $row["PC"];
        $country = $row["country"];
        $text = $row["NAM"];
        $uri = 'tel:'.$row["telephone_number"];

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

$doc->formatOutput = true;

$root = $doc->createElement('EmergencyCallData.SubscriberInfo');
$root->setAttribute('privacyRequested', 'false');
$root->setAttribute('xmlns', 'urn:ietf:params:xml:ns:EmergencyCallData:SubscriberInfo');
$doc->appendChild($root);

$dataProvider = $doc->createElement('DataProviderReference', $dataProviderReference);
$root->appendChild($dataProvider);

$subscriberData = $doc->createElement('SubscriberData');
$root->appendChild($subscriberData);

$vcard = $doc->createElement('vcard');
$vcard->setAttribute('xmlns', 'urn:ietf:params:xml:ns:vcard-4.0');
$subscriberData->appendChild($vcard);

$adr = $doc->createElement('adr');
$vcard->appendChild($adr);

$adr->appendChild($doc->createElement('street', $street_address));
$adr->appendChild($doc->createElement('locality', $locality));
$adr->appendChild($doc->createElement('region', $region));
$adr->appendChild($doc->createElement('code', $code));
$adr->appendChild($doc->createElement('country', $country));

$fn = $doc->createElement('fn');
$fn->appendChild($doc->createElement('text', $text));
$vcard->appendChild($fn);

$lang = $doc->createElement('lang');
$lang->appendChild($doc->createElement('language-tag', 'en'));
$vcard->appendChild($lang);

$tel = $doc->createElement('tel');
$tel->appendChild($doc->createElement('uri', $uri));
$vcard->appendChild($tel);

echo $doc->saveXML();
?>
