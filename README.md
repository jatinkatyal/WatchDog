<h1>WatchDog</h1>
<p>A system to monitor and identify individuals in a controlled environment</p>
<h2>Module <em>Eye</em></h2>
<p>Camera module with a short data of recent people.</p>
<h2>Module <em>Particulars</em></h2>
<p>Data of people, gets updated autonoumously over time.</p>
<h2>Module <em>Sage</em></h2>
<p>System to match visuals of 'Eye' with 'Particulars'.</p>
<h2>Module <em>Detector & pre-processor</em></h2>
<p>Detects face, converts to grayscale performs rescaling & normalization over color space.
Haar cascade from intel's OCVL is used.</p>
<h2>Module <em>Extractor</em></h2>
<p>Linear Binary Pattern extractor.</p>
<h2>Module <em>Mesh</em></h2>
<p>Network to communicate between 'Eyes' and 'Sage'</p>