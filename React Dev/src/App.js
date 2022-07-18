import logo from './logo.svg';
import './App.css';

function App() {
  const urlParams = new URLSearchParams(window.location.search);
  const myParam = urlParams.get('tableNo');
  return (
    <div className="App">
      <header className="App-header">
        <h2>
          This is an Scan an order app for a Restaurant
        </h2>
        <h4>
          You have scaned QR code for table no <span style={{fontSize: 40, color: "dodgerblue"}} >{myParam}</span>
        </h4>
      </header>
    </div>
  );
}

export default App;
