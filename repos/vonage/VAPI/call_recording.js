require("dotenv").config();var express = require('express');
var cors = require('cors');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var app = express();
var url = process.env.URL;


app.use(logger('dev'));
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
app.listen(3000);

const Vonage = require('@vonage/server-sdk');

const vonage = new Vonage({
  apiKey: process.env.API_KEY,
  applicationId: process.env.APPLICATION_ID,
  privateKey: process.env.PRIVATE_KEY
}, {debug: true});

const bodyParser = require('body-parser')

app.use(bodyParser.json())

const onInboundCall = (request, response) => {
  const ncco = [{
      action: 'talk',
      text: 'Welcome to Sreekanth\'s answering service.  Please leave a message and then press #'
    },
    {
      action: 'record',
      endOnKey: '#',
      beepStart: 'true',
      endOnSilence: "3",
      eventUrl: [
        `${request.protocol}://${request.get('host')}/webhooks/recordings`
      ]
    },
    {
      action: 'talk',
      text: 'Thank you for your message. Goodbye.'
    }
  ]

  response.json(ncco)
}

const onRecording = (request, response) => {
  const recording_url = request.body.recording_url
  console.log(`Recording URL = ${recording_url}`)
vonage.files.save(recording_url, recording_url + '.mp3', (err, res) => {
	//recording_url above can be changed to 'sreekanth.mp3'
  if(err) { console.error(err); }
  else {
      console.log(res);
  }
	
	
});

  response.status(204).send()
}

app
  .get('/webhooks/inbound', onInboundCall)
  .post('/webhooks/recordings', onRecording)




