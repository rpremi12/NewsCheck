import React, { Component, useState, useEffect } from 'react';
import { Line,Doughnut } from 'react-chartjs-2';
import Slider from "react-slick";
import { TodoListComponent } from '../apps/TodoList'
import { VectorMap } from "react-jvectormap"

import axios from 'axios'
const mapData = {
  "BZ": 75.00,
  "US": 56.25,
  "AU": 15.45,
  "GB": 25.00,
  "RO": 10.25,
  "GE": 33.25
}


export class Dashboard extends Component {
   
  constructor(props){
    super(props);
    this.state ={
      name:"",
      wname:"",
      wscorel:"N/a",
      wscoreh:"N/a",
      dscore:"N/a",
      transactionHistoryData : {
    labels: ["Negative", "Positive","Neutral"],
    datasets: [{
        data: [55, 25, 20],
        backgroundColor: [
          "#FC424A","#00d25b","#ffab00"
        ]
      }
    ]
  },
   wdata:{

        labels: ['2021-06-06', '2021-06-07', '2021-06-08', '2021-06-09', '2021-06-10', '2021-06-11', '2021-06-12'],
        datasets: [{
          label: '% Positive',
          data: [42.5, 10.0, 30.0, 30.0, 35.0, 22.5, 40.0],
          pointRadius: 6,
          backgroundColor: 
            'rgba(0, 210, 91,0.4)',
          
          borderColor: 
            'rgba(0, 210, 91,0.8)',
          
          borderWidth: 5,
          fill:true
        },
        {
          label: '% Neutral',
          data: [72.5, 62.5, 80.0, 67.5, 72.5, 62.5, 80.0],
                    pointRadius: 6,
          backgroundColor: 
            'rgba(255, 171, 0,0.4)',
          
          borderColor: 
            'rgb(255, 171, 0,0.8)',
          
          borderWidth: 5,
          fill:true
        },
        {
          label: '% Negative',
          data: [100,100,100,100,100,100,100],
                    pointRadius: 4,

          backgroundColor: 
            'rgb(252, 66, 74,0.2)',
          
          borderColor: 
            'rgb(252, 66, 74,0.8)',
          
          borderWidth: 5,
          fill:true
        }]
    }


      //this.onToggleLoop = this.onToggleLoop.bind(this);
  }}


   

    options = {
          responsive: true,

      scales: {
        y:{
          stacked:true
        },
        yAxes: [{
          ticks: {
            beginAtZero: true
          },
          gridLines: {
            color:"rgba(204, 204, 204,0.1)"
          }
        }],
        xAxes: [{
          gridLines: {
            color: "rgba(204, 204, 204,0.1)"
          }
        }]
      },
      legend: {
        display: false
      },
      elements: {
        point: {
          radius: 0
        }
      }
    };
 /*
  componentDidMount() {
    this.getData();
  }*/
  testfunc(){
    var value = document.getElementsByName("search")[0].value;
    console.log(value)
    try{
    this.setState({
      name:'Today\'s Sentiment for \"'+value+'\"',
      transactionHistoryData:{
      labels: [value, "Positive","Neutral"],
      datasets: [{
          data: [55, 25, 20],
          backgroundColor: [
            "#FC424A","#00d25b","#ffab00"
          ]
        }
      ]
    }
    })
  }
  catch(err){
    console.log("didn't work")
  }
  //  this.transactionHistoryData['labels'] = [value, "Positive","Neutral"]
  }

  getData(){
    var apiRes =null;
    var value = document.getElementsByName("search")[0].value;

    try{
    axios.get("http://localhost:5000/get_day?q="+value).then(res =>{
      const name1 = res.data.name
      //console.log(name1)
      apiRes = name1;
      this.setState({
        name:'Today\'s Sentiment for \"'+value+'\"',
        wname:"This Week's Sentiment for \""+value+'\"',
        wscoreh:res.data.maxscore,
        wscorel:res.data.minscore,
        wdata:res.data.wdata,
        transactionHistoryData:res.data.day_data,
        dscore:res.data.dscore

      })

    })
  }
  catch(err){
    apiRes=err.response
  }
  finally{
    console.log(apiRes)
  }

  }


       
  transactionHistoryData =  {
    labels: ["Negative", "Positive","Neutral"],
    datasets: [{
        data: [55, 25, 20],
        backgroundColor: [
          "#FC424A","#00d25b","#ffab00"
        ]
      }
    ]
  };

  transactionHistoryOptions = {
    responsive: true,
    maintainAspectRatio: true,
    segmentShowStroke: false,
    cutoutPercentage: 70,
    elements: {
      arc: {
          borderWidth: 0
      }
    },      
    legend: {
      display: false
    },
    tooltips: {
      enabled: true
    }
  }

  sliderSettings = {
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1
  }

  toggleProBanner() {
    document.querySelector('.proBanner').classList.toggle("hide");
  }
  render () {
    return (
      <div>

      <nav className="navbar p-0 fixed-top d-flex flex-row">

      <div className="navbar-menu-wrapper flex-grow d-flex align-items-stretch">

      <div className="row">
          <ul className="navbar-nav w-100">
            <li className="nav-item w-100">
              <div className="nav-link mt-2 mt-md-0 d-none d-lg-flex search">
                <input name='search' type="text" className="form-control" placeholder="" />
                              <button type="button" onClick={()=>this.getData()} className="btn btn-light btn-fw">Search</button>

              </div>

            </li>
            


          </ul>

        </div></div>
           <ul className="navbar-nav navbar-nav-right">
           </ul>
        </nav>



        <div className="row">
          <div className="col-md-4 grid-margin stretch-card">
            <div className="card">
              <div className="card-body">
                <h4 className="card-title"  >{this.state.name}  </h4>
    
                <div className="aligner-wrapper">
                  <Doughnut redraw={true} data={this.state.transactionHistoryData} options={this.transactionHistoryOptions} />
                  <div className="absolute center-content">
                    <h5 className="font-weight-normal text-whiite text-center mb-2 text-white">{this.state.dscore}</h5>
                    <p className="text-small text-muted text-center mb-0">/100</p>
                  </div>
                </div>  

                      <div className="bg-gray-dark d-flex d-md-block d-xl-flex flex-row py-3 px-4 px-md-3 px-xl-4 rounded mt-3">
                  <div className="text-md-center text-xl-left">
                    <h6 className="mb-1">Negative</h6>
                     <h6 className="mb-1">Neutral</h6>
                    <h6 className="mb-1">Positive</h6>

                   {/* <p className="text-muted mb-0">07 Jan 2019, 09:12AM</p> */}
                  </div>
                  <div className="align-self-center flex-grow text-right text-md-center text-xl-right py-md-2 py-xl-0">
                    <h6 className="font-weight-bold mb-0">{this.state.transactionHistoryData['datasets'][0]['data'][0]}%</h6>
                    <h6 className="font-weight-bold mb-0">{this.state.transactionHistoryData['datasets'][0]['data'][2]}%</h6>
                    <h6 className="font-weight-bold mb-0">{this.state.transactionHistoryData['datasets'][0]['data'][1]}%</h6>

                  </div>
                </div>


              </div>
            </div>
          </div>
          <div className="col-md-8 grid-margin stretch-card">
            <div className="card">
              <div className="card-body">
                <div className="d-flex flex-row justify-content-between">
                  <h4 className="card-title mb-1">{this.state.wname} </h4>
                  <p className="text-muted mb-1"></p>
                </div>
                <div className="row">

<Line data={this.state.wdata} options={this.options} width="450%"/>

                </div>
              </div>
            </div>
          </div>
        </div>
        <div className="row">
          <div className="col-sm-4 grid-margin">
            <div className="card">
              <div className="card-body">
                <h5>Today's Score</h5>
                <div className="row">
                  <div className="col-8 col-sm-12 col-xl-8 my-auto">
                    <div className="d-flex d-sm-block d-md-flex align-items-center">
                      <h2 className="mb-0">{this.state.dscore}</h2>
                        
                       <p className="text-success ml-2 mb-0 font-weight-medium">/100</p>
                    </div>
                   {/* <h6 className="text-muted font-weight-normal">11.38% Since last month</h6>*/}
                  </div>
                  <div className="col-4 col-sm-12 col-xl-4 text-center text-xl-right">
                    <i className="icon-lg mdi mdi-codepen text-primary ml-auto"></i>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div className="col-sm-4 grid-margin">
            <div className="card">
              <div className="card-body">
                <h5>Highest Score of the Week</h5>

                <div className="row">
                  <div className="col-8 col-sm-12 col-xl-8 my-auto">
                    <div className="d-flex d-sm-block d-md-flex align-items-center">
                      <h2 className="mb-0">{this.state.wscoreh}</h2>
                       <p className="text-success ml-2 mb-0 font-weight-medium">/100</p>
                    </div>
                    <h6 className="text-muted font-weight-normal"></h6>
                  </div>
                  <div className="col-4 col-sm-12 col-xl-4 text-center text-xl-right">
                                      <i className="icon-lg mdi mdi-monitor text-success ml-auto"></i>

                  </div>
                </div>
              </div>
            </div>
          </div>
          <div className="col-sm-4 grid-margin">
            <div className="card">
              <div className="card-body">
                <h5>Lowest Score of the Week</h5>
                <div className="row">
                  <div className="col-8 col-sm-12 col-xl-8 my-auto">
                    <div className="d-flex d-sm-block d-md-flex align-items-center">
                      <h2 className="mb-0">{this.state.wscorel}</h2>
                      <p className="text-danger ml-2 mb-0 font-weight-medium">/100</p>
                    </div>
                    <h6 className="text-muted font-weight-normal"></h6>
                  </div>
                  <div className="col-4 col-sm-12 col-xl-4 text-center text-xl-right">
                                      <i className="icon-lg mdi mdi-wallet-travel text-danger ml-auto"></i>

                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        
        <div className="row">
          <div className="col-12">
            <div className="card">
              <div className="card-body">
                <h4 className="card-title">Articles by Countries</h4>
                <div className="row">
                  <div className="col-md-5">
                    <div className="table-responsive">
                      <table className="table">
                        <tbody>
                          <tr>
                            <td>
                              <i className="flag-icon flag-icon-us"></i>
                            </td>
                            <td>USA</td>
                            <td className="text-right"> 1500 </td>
                            <td className="text-right font-weight-medium"> 56.35% </td>
                          </tr>
                          <tr>
                            <td>
                              <i className="flag-icon flag-icon-de"></i>
                            </td>
                            <td>Germany</td>
                            <td className="text-right"> 800 </td>
                            <td className="text-right font-weight-medium"> 33.25% </td>
                          </tr>
                          <tr>
                            <td>
                              <i className="flag-icon flag-icon-au"></i>
                            </td>
                            <td>Australia</td>
                            <td className="text-right"> 760 </td>
                            <td className="text-right font-weight-medium"> 15.45% </td>
                          </tr>
                          <tr>
                            <td>
                              <i className="flag-icon flag-icon-gb"></i>
                            </td>
                            <td>United Kingdom</td>
                            <td className="text-right"> 450 </td>
                            <td className="text-right font-weight-medium"> 25.00% </td>
                          </tr>
                          <tr>
                            <td>
                              <i className="flag-icon flag-icon-ro"></i>
                            </td>
                            <td>Romania</td>
                            <td className="text-right"> 620 </td>
                            <td className="text-right font-weight-medium"> 10.25% </td>
                          </tr>
                          <tr>
                            <td>
                              <i className="flag-icon flag-icon-br"></i>
                            </td>
                            <td>Brasil</td>
                            <td className="text-right"> 230 </td>
                            <td className="text-right font-weight-medium"> 75.00% </td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                  </div>
                  <div className="col-md-7">
                    <div id="audience-map" className="vector-map"></div>
                    <VectorMap
                    map={"world_mill"}
                    backgroundColor="transparent" //change it to ocean blue: #0077be
                    panOnDrag={true}
                    containerClassName="dashboard-vector-map"
                    focusOn= { {
                      x: 0.5,
                      y: 0.5,
                      scale: 1,
                      animate: true
                    }}
                    series={{
                      regions: [{
                        scale: ['#3d3c3c', '#f2f2f2'],
                        normalizeFunction: 'polynomial',
                        values: mapData
                      }]
                    }}
                  />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div> 
    );
  }
}

export default Dashboard;