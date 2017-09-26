import React, { Component } from 'react';
import Button from './Button';
import './MapMenu.css';

export default class MapMenu extends Component {
  constructor(props) {
    super(props);
  }

  handleButtonClick(e) {
    var clicked = e.target.getAttribute('id');

    if (clicked === 'button-start-game') {
      this.props.switchView('mapmenu');
    }
  }

  render() {
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
                handleClick={this.handleButtonClick.bind(this)} />

              <div id="map-info">

                <div className="section">
                  <div className="section-header">
                    Pile Types and Amounts
                  </div>
                  <div className="section-list-item">
                    <div className="section-list-item-name">
                      Birch Sawlog
                    </div>
                    <div className="section-list-item-value">
                      3
                    </div>
                  </div>
                  <div className="section-list-item">
                    <div className="section-list-item-name">
                      Birch Pulp
                    </div>
                    <div className="section-list-item-value">
                      22
                    </div>
                  </div>
                  <div className="section-list-item">
                    <div className="section-list-item-name">
                      Pine Pulp
                    </div>
                    <div className="section-list-item-value">
                      31
                    </div>
                  </div>
                  <div className="section-list-item">
                    <div className="section-list-item-name">
                      Spruce Pulp
                    </div>
                    <div className="section-list-item-value">
                      3
                    </div>
                  </div>
                </div>

                <div className="section">
                  <div className="section-header">
                    Route Length
                  </div>
                  <div className="section-value">
                    4184.3 m
                  </div>
                </div>

                <div className="section">
                  <div className="section-header">
                    Storage Area Amount
                  </div>
                  <div className="section-value">
                    3
                  </div>
                </div>

                <div className="section">
                  <div className="section-header">
                    Passing Limit
                  </div>
                  <div className="section-value">
                    NO
                  </div>
                </div>

              </div>

              <Button
                id="button-start-game"
                text="Start game"
                style={{backgroundColor: 'var(--jd-yellow)'}}
                handleClick={this.handleButtonClick.bind(this)} />

            </div>

            <div id="right">
              <div className="map-chevron map-chevron-inactive" id="map-chevron-left">
                {'<'}
              </div>
              <div className="map-chevron" id="map-chevron-right">
                {'>'}
              </div>
            </div>

          </div>

          <div id="bottom-row">
            1/20
          </div>

        </div>

      </div>
    );
  }
}
