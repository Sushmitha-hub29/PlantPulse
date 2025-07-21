import { useState } from 'react';

function App() {
  const [image, setImage] = useState(null);
  const [prediction, setPrediction] = useState(null);

  const handleImageChange = (e) => {
    setImage(e.target.files[0]);
    setPrediction(null); // reset prediction
  };

  const handleUpload = async () => {
    if (!image) return;

    const formData = new FormData();
    formData.append('image', image);

    try {
      const response = await fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        body: formData
      });

      const data = await response.json();
      setPrediction(data);
    } catch (error) {
      console.error('Upload failed:', error);
    }
  };

  return (
    <div style={{ padding: 30 }}>
      <h1>🍱 Food Recognition & Calorie Estimator</h1>
      <input type="file" accept="image/*" onChange={handleImageChange} />
      <br /><br />
      <button onClick={handleUpload}>Predict</button>

      {prediction && (
        <div style={{ marginTop: 20 }}>
          <h3>🍽️ Prediction:</h3>
          <p><strong>Food:</strong> {prediction.food}</p>
          <p><strong>Estimated Calories:</strong> {prediction.calories}</p>
        </div>
      )}
    </div>
  );
}

export default App;
