import React from 'react';
import logo from './logo.svg';
import './App.css';
// to push to GitHub in the terminal run this:
// git add . the period says what you want to add and stages it for commitment to github
// git status tells you what has or has not been adds
// git commit -m "message you want to give" the -m is message
// git push sends things from my computer up to github
// git pull brings things in from github
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to words to add
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
