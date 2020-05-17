import React from 'react';
import './App.css';
import axios from 'axios';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: 'Some sample text wohoo!'
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    event.preventDefault();
    let value = this.state.value;
    axios({
      method: 'post',
      url: '/magicwords',
      data: {
        value,
      }
    })
    .then(res => {
      let magicWords = res.data.data;
      this.setState({value: magicWords})
    })
  }


  render() {
    return (
      <div className="wrapper">
        <div className="formWrapper">
          <input className="textbox" type="text" value={this.state.value} onChange={this.handleChange} />
        </div>
        <button className="submitBtn" onClick={this.handleSubmit}>
          Button
        </button>
      </div>
    );
  }
}

export default App;
