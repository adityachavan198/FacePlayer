const express = require("express");
const bodyParser = require("body-parser");
const ejs = require("ejs");
var SpotifyWebApi = require('spotify-web-api-node');

const app = express();
app.set('view engine', 'ejs');

app.use(express.urlencoded({
  extended: false
}));

app.use(express.static("public"));

var spotifyApi = new SpotifyWebApi({
  clientId: '7c9797aa79d84806807faedc20b6e647',
  clientSecret: '0bdd2e5c0e7341b48e1f7f3b903825d8',
  redirectUri: 'http://www.example.com/callback'
});
spotifyApi.setAccessToken('BQDlTLvd3xG53hELW5Zx0qe5-aoB8ogPO0Kggn66VAPuwyqLMWtNpsi23d1-c8eYucuG5bgsvQnZCXDfGuUcD-vdxwXp3rVDk9RqogpIcHBEF3quXdDop74_2ibtW1sYZccRr69KVOSNst7qjN3hHTA2WtfjVo9qvy3Kvtvsajw_5AfnUeY');


spotifyApi.clientCredentialsGrant().then(
    function (data) {
        console.log('The access token expires in ' + data.body.access_token);
        console.log('The access token is ' + data.body.access_token);

        // Save the access token so that it's used in future calls
        spotifyApi.setAccessToken(data.body.access_token);
    },
    function (err) {
        console.log(
            'Something went wrong when retrieving an access token',
            err.message
        );
    }
);

// var name = "";
// var image = "";
//
// var obj = "";
// var tc = "";
// var album = "";



// app.get("/",function(req,res){
//   res.render("index",{
//     h: obj,
//     n: name,
//     img: image,
//   })
// })

// app.post("/search", function(req, res) {
//   tc = req.body.track;
//   spotifyApi.getUserPlaylists(tc)
//     .then(function(data) {
//       name = data.body;
//       image = data.body;
//       console.log(name);
//       console.log(image);
//       var trackName = data.body;
//       obj = trackName;
//       res.redirect("/")
//       console.log('Search by "Love"', data.body);
//     }, function(err) {
//       console.error(err);
//     });;
// })

// app.get('/search/:data', function(req, res) {
//   console.log('search word ' + req.params.data);
//   spotifyApi.getUserPlaylists(name)
//     .then(function(data) {
//       var user = data.body;
//       console.log(user);
//       res.render("new", {
//         he: trackName
//       });
//     }, function(err) {
//       console.error(err);
//     });
// });

var playlists =  [];
var play1 = ""
var tracks_name = [];
var tracks_audio =[];
var tracks_image =[];
var i=0;
var j=0;
app.get("/", (req,res)=>{

  res.render("index" ,{
    playlists: playlists,
    play1 : play1,
    tracks_name : tracks_name,
    tracks_audio : tracks_audio,
    tracks_image : tracks_image
  })

  console.log(playlists);
})


  spotifyApi.getUserPlaylists('joab4qf54hmmc19t23jmj7i1h')
    .then(function(data) {

        while(data.body.items[i] != undefined){
          playlists.push(data.body.items[i].id)
          i++;
        }
        for ( j = 0; j < playlists.length; j++) {
          spotifyApi.getPlaylist(playlists[j])
            .then(function(data) {
                for (var k = 0; k < 10; k++) {
                  if (data.body.tracks.items[k].track.preview_url != null && tracks_name.includes(data.body.tracks.items[k].track.preview_url) != true  ) {
                        tracks_name.push(data.body.tracks.items[k].track.name)
                        tracks_audio.push(data.body.tracks.items[k].track.preview_url)
                        tracks_image.push(data.body.images[1].url)
                        // tracks_image.push(data.body.images[k].url)
                  }
                }
                // && data.body.images[k].url !=undefined
              ;
              console.log(tracks_image);
              // console.log(tracks_name);
              // console.log(tracks_audio);
            }, function(err) {
              console.log('Something went wrong!', err);
            });
        }
        // console.log(play1);
        // console.log(playlists);
    },function(err) {
      console.log('Something went wrong!', err);
    });






app.listen("80", (req,res)=>{
  console.log("Server started");
})
