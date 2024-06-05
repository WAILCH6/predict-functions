const functions = require('firebase-functions');
const admin = require('firebase-admin');
const { spawn } = require('child_process');
const path = require('path');

admin.initializeApp();

const modelPath = path.join(__dirname, 'random_forest_model.pkl');

exports.predict = functions.https.onRequest((request, response) => {
    const heure = request.body.heure;

    const pythonProcess = spawn('python', ['predict.py', modelPath, heure]);

    pythonProcess.stdout.on('data', (data) => {
        response.send(data.toString());
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
    });

    pythonProcess.on('close', (code) => {
        console.log(`child process exited with code ${code}`);
    });
});
