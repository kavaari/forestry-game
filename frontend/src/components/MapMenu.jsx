import React, { Component } from 'react';
import Button from './Button';
import './MapMenu.css';

var dummyMaps = [
  {
    name: 'Map with 4 types',
    image: 'https://placekitten.com/1001/601',
    pileTypes: [
      {
        name: 'Birch Sawlog',
        amount: 3
      },
      {
        name: 'Birch Pulp',
        amount: 22
      },
      {
        name: 'Pine Pulp',
        amount: 31
      },
      {
        name: 'Spruce Pulp',
        amount: 3
      }
    ],
    routeLength: 4184.3,
    storageAreas: 3,
    passingLimit: false
  },
  {
    name: 'Another map',
    image: 'https://placekitten.com/801/701',
    pileTypes: [
      {
        name: 'Pine Sawlog',
        amount: 45
      },
      {
        name: 'Mystery Wood',
        amount: 99
      }
    ],
    routeLength: 234.1,
    storageAreas: 1,
    passingLimit: false
  },
  {
    name: 'Third map\'s the charm',
    image: 'https://placekitten.com/1101/401',
    pileTypes: [
      {
        name: 'Pine Pulp',
        amount: 1
      }
    ],
    routeLength: 9000.1,
    storageAreas: 50,
    passingLimit: false
  }
];

export default class MapMenu extends Component {
  constructor(props) {
    super(props);
    this.state = {
      maps: dummyMaps,
      selectedMapIndex: 0
    }
  }

  handleButtonClick(e) {
    var clicked = e.target.getAttribute('id');

    if (clicked === 'button-back') {
      this.props.switchView('mainmenu');
    }
  }

  handlePreviousClick() {
    if (this.state.selectedMapIndex === 0) {

      this.setState({
        selectedMapIndex: this.state.maps.length - 1
      });
    
    } else {

      this.setState((prevState) => ({
        selectedMapIndex: prevState.selectedMapIndex - 1
      }));
    }
  }

  handleNextClick() {
    if (this.state.selectedMapIndex === this.state.maps.length - 1) {

      this.setState({
        selectedMapIndex: 0
      });
    
    } else {

      this.setState((prevState) => ({
        selectedMapIndex: prevState.selectedMapIndex + 1
      }));
    }

  }

  render() {

    var selMap = this.state.maps[this.state.selectedMapIndex];

    var pileTypes = selMap.pileTypes.map(pileType => 
      <div className="section-list-item" key={pileType.name}>
        <div className="section-list-item-name">
          {pileType.name}
        </div>
        <div className="section-list-item-value">
          {pileType.amount}
        </div>
      </div>
    );

    var mapImage = {
      backgroundImage: 'url(' + selMap.image + ')'
    };

    var firstMap = this.state.selectedMapIndex === 0 ? true : false;
    var lastMap = this.state.selectedMapIndex === this.state.maps.length - 1 ? true : false;

    return (
      <div className="MapMenu">
        
        <div id="map-menu">

          <div id="top">

            <div id="left">

              <Button
                id="button-back"
                text="Back to menu"
                handleClick={this.handleButtonClick.bind(this)} />

              <Button
                id="button-create-map"
                text="Create map"
                handleClick={this.handleButtonClick.bind(this)}
                inactive={this.props.loggedIn ? false : true} />

              <div id="map-info">

                <div className="section">

                  <div className="section-header">
                    Pile Types and Amounts
                  </div>

                  {pileTypes}

                </div>

                <div className="section">

                  <div className="section-header">
                    Route Length
                  </div>

                  <div className="section-value">
                    {selMap.routeLength + ' m'}
                  </div>

                </div>

                <div className="section">

                  <div className="section-header">
                    Storage Area Amount
                  </div>

                  <div className="section-value">
                    {selMap.storageAreas}
                  </div>

                </div>

                <div className="section">

                  <div className="section-header">
                    Passing Limit
                  </div>

                  <div className="section-value">
                    {selMap.passingLimit ? 'YES' : 'NO'}
                  </div>

                </div>

              </div>

              <Button
                id="button-start-game"
                text="Start game"
                style={{backgroundColor: 'var(--jd-yellow)'}}
                handleClick={this.handleButtonClick.bind(this)} />

            </div>

            <div
              id="right"
              style={mapImage} >

              <div id="map-name">
                {selMap.name}
              </div>

              <div
                className={firstMap ? 'map-chevron map-chevron-inactive' : 'map-chevron'}
                id="map-chevron-left"
                onClick={firstMap ? '' : this.handlePreviousClick.bind(this)} >

                {'<'}

              </div>

              <div
                className={lastMap ? 'map-chevron map-chevron-inactive' : 'map-chevron'}
                id="map-chevron-right"
                onClick={lastMap ? '' : this.handleNextClick.bind(this)} >

                {'>'}

              </div>

            </div>

          </div>

          <div id="bottom-row">
            {(this.state.selectedMapIndex + 1) + '/' + this.state.maps.length}
          </div>

        </div>

      </div>
    );
  }
}
