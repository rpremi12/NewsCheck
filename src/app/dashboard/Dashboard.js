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

/*
componentWillUnmount() {
        clearInterval(this.timer);
        this.timer = null;
    }*/

/*
async fetchUsersAsync() {

  const [data, setData] = useState(0)
        try {
            this.setState({...this.state, isFetching: true});
            const response = await axios.get('/simple_chart');
            this.setState({users: response.data, isFetching: false});
        } catch (e) {
            console.log(e);
            this.setState({...this.state, isFetching: false});
        }
    };
fetchUsers = this.fetchUsersAsync;*/
       
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
      {/*
        <div className="proBanner">
          <div>
            <span className="d-flex align-items-center purchase-popup">
              <p>Get tons of UI components, Plugins, multiple layouts, 20+ sample pages, and more!</p>
              <a href="https://www.bootstrapdash.com/product/corona-react/?utm_source=organic&utm_medium=banner&utm_campaign=free-preview" rel="noopener noreferrer" target="_blank" className="btn btn-sm purchase-button ml-auto">Check Pro Version</a>
              <i className="mdi mdi-close bannerClose" onClick={this.toggleProBanner}></i>
            </span>
          </div>
        </div>
      */}
      {/*
        <div className="row">
          <div className="col-12 grid-margin stretch-card">
            <div className="card corona-gradient-card">
              <div className="card-body py-0 px-0 px-sm-3">
                <div className="row align-items-center">
                  <div className="col-4 col-sm-3 col-xl-2">
                    <img src={require('../../assets/images/dashboard/Group126@2x.png')} className="gradient-corona-img img-fluid" alt="banner" />
                  </div>
                  <div className="col-5 col-sm-7 col-xl-8 p-0">
                    <h4 className="mb-1 mb-sm-0">New refreshing look</h4>
                    <p className="mb-0 font-weight-normal d-none d-sm-block">Corona admin template now with a new facelift for enhanced legibility and aesthetics!</p>
                  </div>
                  <div className="col-3 col-sm-2 col-xl-2 pl-0 text-center">
                    <button className="btn btn-outline-light btn-rounded get-started-btn">Get Started</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>*/}
        
        {/*
        <div className="row">
          <div className="col-xl-3 col-sm-6 grid-margin stretch-card">
            <div className="card">
              <div className="card-body">
                <div className="row">
                  <div className="col-9">
                    <div className="d-flex align-items-center align-self-start">
                      <h3 className="mb-0">$12.34</h3>
                      <p className="text-success ml-2 mb-0 font-weight-medium">+3.5%</p>
                    </div>
                  </div>
                  <div className="col-3">
                    <div className="icon icon-box-success ">
                      <span className="mdi mdi-arrow-top-right icon-item"></span>
                    </div>
                  </div>
                </div>
                <h6 className="text-muted font-weight-normal">Potential growth</h6>
              </div>
            </div>
          </div>
          <div className="col-xl-3 col-sm-6 grid-margin stretch-card">
            <div className="card">
              <div className="card-body">
                <div className="row">
                  <div className="col-9">
                    <div className="d-flex align-items-center align-self-start">
                      <h3 className="mb-0">$17.34</h3>
                      <p className="text-success ml-2 mb-0 font-weight-medium">+11%</p>
                    </div>
                  </div>
                  <div className="col-3">
                    <div className="icon icon-box-success">
                      <span className="mdi mdi-arrow-top-right icon-item"></span>
                    </div>
                  </div>
                </div>
                <h6 className="text-muted font-weight-normal">Revenue current</h6>
              </div>
            </div>
          </div>
          <div className="col-xl-3 col-sm-6 grid-margin stretch-card">
            <div className="card">
              <div className="card-body">
                <div className="row">
                  <div className="col-9">
                    <div className="d-flex align-items-center align-self-start">
                      <h3 className="mb-0">$12.34</h3>
                      <p className="text-danger ml-2 mb-0 font-weight-medium">-2.4%</p>
                    </div>
                  </div>
                  <div className="col-3">
                    <div className="icon icon-box-danger">
                      <span className="mdi mdi-arrow-bottom-left icon-item"></span>
                    </div>
                  </div>
                </div>
                <h6 className="text-muted font-weight-normal">Daily Income</h6>
              </div>
            </div>
          </div>
          <div className="col-xl-3 col-sm-6 grid-margin stretch-card">
            <div className="card">
              <div className="card-body">
                <div className="row">
                  <div className="col-9">
                    <div className="d-flex align-items-center align-self-start">
                      <h3 className="mb-0">$31.53</h3>
                      <p className="text-success ml-2 mb-0 font-weight-medium">+3.5%</p>
                    </div>
                  </div>
                  <div className="col-3">
                    <div className="icon icon-box-success ">
                      <span className="mdi mdi-arrow-top-right icon-item"></span>
                    </div>
                  </div>
                </div>
                <h6 className="text-muted font-weight-normal">Expense current</h6>
              </div>
            </div>
          </div>
        </div>
      */}
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
                {/*
                  <div className="col-12">
                    <div className="preview-list">
                      <div className="preview-item border-bottom">
                        <div className="preview-thumbnail">
                          <div className="preview-icon bg-primary">
                            <i className="mdi mdi-file-document"></i>
                          </div>
                        </div>
                        <div className="preview-item-content d-sm-flex flex-grow">
                          <div className="flex-grow">
                            <h6 className="preview-subject">Admin dashboard design</h6>
                            <p className="text-muted mb-0">Broadcast web app mockup</p>
                          </div>
                          <div className="mr-auto text-sm-right pt-2 pt-sm-0">
                            <p className="text-muted">15 minutes ago</p>
                            <p className="text-muted mb-0">30 tasks, 5 issues </p>
                          </div>
                        </div>
                      </div>
                      <div className="preview-item border-bottom">
                        <div className="preview-thumbnail">
                          <div className="preview-icon bg-success">
                            <i className="mdi mdi-cloud-download"></i>
                          </div>
                        </div>
                        <div className="preview-item-content d-sm-flex flex-grow">
                          <div className="flex-grow">
                            <h6 className="preview-subject">Wordpress Development</h6>
                            <p className="text-muted mb-0">Upload new design</p>
                          </div>
                          <div className="mr-auto text-sm-right pt-2 pt-sm-0">
                            <p className="text-muted">1 hour ago</p>
                            <p className="text-muted mb-0">23 tasks, 5 issues </p>
                          </div>
                        </div>
                      </div>
                      <div className="preview-item border-bottom">
                        <div className="preview-thumbnail">
                          <div className="preview-icon bg-info">
                            <i className="mdi mdi-clock"></i>
                          </div>
                        </div>
                        <div className="preview-item-content d-sm-flex flex-grow">
                          <div className="flex-grow">
                            <h6 className="preview-subject">Project meeting</h6>
                            <p className="text-muted mb-0">New project discussion</p>
                          </div>
                          <div className="mr-auto text-sm-right pt-2 pt-sm-0">
                            <p className="text-muted">35 minutes ago</p>
                            <p className="text-muted mb-0">15 tasks, 2 issues</p>
                          </div>
                        </div>
                      </div>
                      <div className="preview-item border-bottom">
                        <div className="preview-thumbnail">
                          <div className="preview-icon bg-danger">
                            <i className="mdi mdi-email-open"></i>
                          </div>
                        </div>
                        <div className="preview-item-content d-sm-flex flex-grow">
                          <div className="flex-grow">
                            <h6 className="preview-subject">Broadcast Mail</h6>
                            <p className="text-muted mb-0">Sent release details to team</p>
                          </div>
                          <div className="mr-auto text-sm-right pt-2 pt-sm-0">
                            <p className="text-muted">55 minutes ago</p>
                            <p className="text-muted mb-0">35 tasks, 7 issues </p>
                          </div>
                        </div>
                      </div>
                      <div className="preview-item">
                        <div className="preview-thumbnail">
                          <div className="preview-icon bg-warning">
                            <i className="mdi mdi-chart-pie"></i>
                          </div>
                        </div>
                        <div className="preview-item-content d-sm-flex flex-grow">
                          <div className="flex-grow">
                            <h6 className="preview-subject">UI Design</h6>
                            <p className="text-muted mb-0">New application planning</p>
                          </div>
                          <div className="mr-auto text-sm-right pt-2 pt-sm-0">
                            <p className="text-muted">50 minutes ago</p>
                            <p className="text-muted mb-0">27 tasks, 4 issues </p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>*/}
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

        {/*
        <div className="row ">
          <div className="col-12 grid-margin">
            <div className="card">
              <div className="card-body">
                <h4 className="card-title">Order Status</h4>
                <div className="table-responsive">
                  <table className="table">
                    <thead>
                      <tr>
                        <th>
                          <div className="form-check form-check-muted m-0">
                            <label className="form-check-label">
                              <input type="checkbox" className="form-check-input" />
                              <i className="input-helper"></i>
                            </label>
                          </div>
                        </th>
                        <th> Client Name </th>
                        <th> Order No </th>
                        <th> Product Cost </th>
                        <th> Project </th>
                        <th> Payment Mode </th>
                        <th> Start Date </th>
                        <th> Payment Status </th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>
                          <div className="form-check form-check-muted m-0">
                            <label className="form-check-label">
                              <input type="checkbox" className="form-check-input" />
                              <i className="input-helper"></i>
                            </label>
                          </div>
                        </td>
                        <td>
                          <div className="d-flex">
                            <img src={require('../../assets/images/faces/face1.jpg')} alt="face" />
                            <span className="pl-2">Henry Klein</span>
                          </div>
                        </td>
                        <td> 02312 </td>
                        <td> $14,500 </td>
                        <td> Dashboard </td>
                        <td> Credit card </td>
                        <td> 04 Dec 2019 </td>
                        <td>
                          <div className="badge badge-outline-success">Approved</div>
                        </td>
                      </tr>
                      <tr>
                        <td>
                          <div className="form-check form-check-muted m-0">
                            <label className="form-check-label">
                              <input type="checkbox" className="form-check-input" />
                              <i className="input-helper"></i>
                            </label>
                          </div>
                        </td>
                        <td>
                          <div className="d-flex">
                            <img src={require('../../assets/images/faces/face2.jpg')} alt="face" />
                            <span className="pl-2">Estella Bryan</span>
                          </div>
                        </td>
                        <td> 02312 </td>
                        <td> $14,500 </td>
                        <td> Website </td>
                        <td> Cash on delivered </td>
                        <td> 04 Dec 2019 </td>
                        <td>
                          <div className="badge badge-outline-warning">Pending</div>
                        </td>
                      </tr>
                      <tr>
                        <td>
                          <div className="form-check form-check-muted m-0">
                            <label className="form-check-label">
                              <input type="checkbox" className="form-check-input" />
                              <i className="input-helper"></i>
                            </label>
                          </div>
                        </td>
                        <td>
                          <div className="d-flex">
                            <img src={require('../../assets/images/faces/face5.jpg')} alt="face" />
                            <span className="pl-2">Lucy Abbott</span>
                          </div>
                        </td>
                        <td> 02312 </td>
                        <td> $14,500 </td>
                        <td> App design </td>
                        <td> Credit card </td>
                        <td> 04 Dec 2019 </td>
                        <td>
                          <div className="badge badge-outline-danger">Rejected</div>
                        </td>
                      </tr>
                      <tr>
                        <td>
                          <div className="form-check form-check-muted m-0">
                            <label className="form-check-label">
                              <input type="checkbox" className="form-check-input" />
                              <i className="input-helper"></i>
                            </label>
                          </div>
                        </td>
                        <td>
                          <div className="d-flex">
                            <img src={require('../../assets/images/faces/face3.jpg')} alt="face" />
                            <span className="pl-2">Peter Gill</span>
                          </div>
                        </td>
                        <td> 02312 </td>
                        <td> $14,500 </td>
                        <td> Development </td>
                        <td> Online Payment </td>
                        <td> 04 Dec 2019 </td>
                        <td>
                          <div className="badge badge-outline-success">Approved</div>
                        </td>
                      </tr>
                      <tr>
                        <td>
                          <div className="form-check form-check-muted m-0">
                            <label className="form-check-label">
                              <input type="checkbox" className="form-check-input" />
                              <i className="input-helper"></i>
                            </label>
                          </div>
                        </td>
                        <td>
                          <div className="d-flex">
                            <img src={require('../../assets/images/faces/face4.jpg')} alt="face" />
                            <span className="pl-2">Sallie Reyes</span>
                          </div>
                        </td>
                        <td> 02312 </td>
                        <td> $14,500 </td>
                        <td> Website </td>
                        <td> Credit card </td>
                        <td> 04 Dec 2019 </td>
                        <td>
                          <div className="badge badge-outline-success">Approved</div>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div className="row">
          <div className="col-md-6 col-xl-4 grid-margin stretch-card">
            <div className="card">
              <div className="card-body">
                <div className="d-flex flex-row justify-content-between">
                  <h4 className="card-title">Messages</h4>
                  <p className="text-muted mb-1 small">View all</p>
                </div>
                <div className="preview-list">
                  <div className="preview-item border-bottom">
                    <div className="preview-thumbnail">
                      <img src={require('../../assets/images/faces/face6.jpg')} alt="face" className="rounded-circle" />
                    </div>
                    <div className="preview-item-content d-flex flex-grow">
                      <div className="flex-grow">
                        <div className="d-flex d-md-block d-xl-flex justify-content-between">
                          <h6 className="preview-subject">Leonard</h6>
                          <p className="text-muted text-small">5 minutes ago</p>
                        </div>
                        <p className="text-muted">Well, it seems to be working now.</p>
                      </div>
                    </div>
                  </div>
                  <div className="preview-item border-bottom">
                    <div className="preview-thumbnail">
                      <img src={require('../../assets/images/faces/face8.jpg')} alt="face" className="rounded-circle" />
                    </div>
                    <div className="preview-item-content d-flex flex-grow">
                      <div className="flex-grow">
                        <div className="d-flex d-md-block d-xl-flex justify-content-between">
                          <h6 className="preview-subject">Luella Mills</h6>
                          <p className="text-muted text-small">10 Minutes Ago</p>
                        </div>
                        <p className="text-muted">Well, it seems to be working now.</p>
                      </div>
                    </div>
                  </div>
                  <div className="preview-item border-bottom">
                    <div className="preview-thumbnail">
                      <img src={require('../../assets/images/faces/face9.jpg')} alt="face" className="rounded-circle" />
                    </div>
                    <div className="preview-item-content d-flex flex-grow">
                      <div className="flex-grow">
                        <div className="d-flex d-md-block d-xl-flex justify-content-between">
                          <h6 className="preview-subject">Ethel Kelly</h6>
                          <p className="text-muted text-small">2 Hours Ago</p>
                        </div>
                        <p className="text-muted">Please review the tickets</p>
                      </div>
                    </div>
                  </div>
                  <div className="preview-item border-bottom">
                    <div className="preview-thumbnail">
                      <img src={require('../../assets/images/faces/face11.jpg')} alt="face" className="rounded-circle" />
                    </div>
                    <div className="preview-item-content d-flex flex-grow">
                      <div className="flex-grow">
                        <div className="d-flex d-md-block d-xl-flex justify-content-between">
                          <h6 className="preview-subject">Herman May</h6>
                          <p className="text-muted text-small">4 Hours Ago</p>
                        </div>
                        <p className="text-muted">Thanks a lot. It was easy to fix it .</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div className="col-md-6 col-xl-4 grid-margin stretch-card">
            <div className="card">
              <div className="card-body">
                <h4 className="card-title">Portfolio Slide</h4>
                <Slider className="portfolio-slider" {...this.sliderSettings}>
                  <div className="item">
                    <img src={require('../../assets/images/dashboard/Rectangle.jpg')} alt="carousel-item" />
                  </div>
                  <div className="item">
                    <img src={require('../../assets/images/dashboard/Img_5.jpg')} alt="carousel-item" />
                  </div>
                  <div className="item">
                    <img src={require('../../assets/images/dashboard/img_6.jpg')} alt="carousel-item" />
                  </div>
                </Slider>
                <div className="d-flex py-4">
                  <div className="preview-list w-100">
                    <div className="preview-item p-0">
                      <div className="preview-thumbnail">
                        <img src={require('../../assets/images/faces/face12.jpg')} className="rounded-circle" alt="face" />
                      </div>
                      <div className="preview-item-content d-flex flex-grow">
                        <div className="flex-grow">
                          <div className="d-flex d-md-block d-xl-flex justify-content-between">
                            <h6 className="preview-subject">CeeCee Bass</h6>
                            <p className="text-muted text-small">4 Hours Ago</p>
                          </div>
                          <p className="text-muted">Well, it seems to be working now.</p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <p className="text-muted">Well, it seems to be working now. </p>
                <div className="progress progress-md portfolio-progress">
                  <div className="progress-bar bg-success" role="progressbar" style={{width: '50%'}} aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
                </div>
              </div>
            </div>
          </div>
          <div className="col-md-12 col-xl-4 grid-margin stretch-card">
            <div className="card">
              <div className="card-body">
                <h4 className="card-title">To do list</h4>
                <TodoListComponent />
              </div>
            </div>
          </div>
        </div>
      */}
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