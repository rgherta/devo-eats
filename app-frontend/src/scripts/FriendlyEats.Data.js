/**
 * Copyright 2017 Google Inc. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
'use strict';
//${location.protocol}//${location.host}
const restaurants_api = `/microservice-restaurants`
const ratings_api = `/microservice-ratings`

FriendlyEats.prototype.addRestaurant = function (data) {
  const collection = firebase.firestore().collection('restaurants');
  return collection.add(data);
};

FriendlyEats.prototype.getAllRestaurants = function (render) {
  // const query = firebase.firestore()
  //   .collection('restaurants')
  //   .orderBy('avgRating', 'desc')
  //   .limit(50);
  // this.getDocumentsInQuery(query, render);

  fetch(`${restaurants_api}/list`)
  .then(response => {
    console.log(response)
    return response.json()})
  .then(result => {
    console.log(result)
    result.sort((a,b) => b.avgRating - a.avgRating)
    result = result.slice(0, 50)
    this.getDocumentsInQuery(result, render);
  })


};

FriendlyEats.prototype.getDocumentsInQuery = function (elements, render) {

  elements.forEach( (element) => {
    return render(element)
  })

  // query.onSnapshot((snapshot) => {
  //   if (!snapshot.size) {
  //     return render();
  //   }

  //   snapshot.docChanges().forEach((change) => {
  //     if (change.type === 'added' || change.type === 'modified') {
  //       render(change.doc);
  //     }
  //   });
  // });
};

FriendlyEats.prototype.getRestaurant = async (id) => {
  //console.log(id)
  //return firebase.firestore().collection('restaurants').doc(id).get();
  let response = await fetch(`${restaurants_api}/list?id=${id}`)
  let data = await response.json()
  console.log("requesting id", id, response, data)
  return data
};

// FriendlyEats.prototype.getRatings= async (id) => {
//   //console.log(id)
//   //return firebase.firestore().collection('restaurants').doc(id).get();
//   let response = await fetch(`${restaurants_api}/ratings?id=${id}`)
//   let data = await response.json()
//   console.log("requesting id", id, response, data)
//   return data
// };

FriendlyEats.prototype.getFilteredRestaurants = function (filters, render) {
  let query = firebase.firestore().collection('restaurants');

  if (filters.category !== 'Any') {
    query = query.where('category', '==', filters.category);
  }

  if (filters.city !== 'Any') {
    query = query.where('city', '==', filters.city);
  }

  if (filters.price !== 'Any') {
    query = query.where('price', '==', filters.price.length);
  }

  if (filters.sort === 'Rating') {
    query = query.orderBy('avgRating', 'desc');
  } else if (filters.sort === 'Reviews') {
    query = query.orderBy('numRatings', 'desc');
  }

  this.getDocumentsInQuery(query, render);
};

FriendlyEats.prototype.addRating = async (restaurantID, rating) => {
  //const collection = firebase.firestore().collection('restaurants');
  //const document = collection.doc(restaurantID);
  //const newRatingDocument = document.collection('ratings').doc();

  // return firebase.firestore().runTransaction((transaction) => {
  //   return transaction.get(document).then((doc) => {
  //     const data = doc.data();

  //     const newAverage =
  //         (data.numRatings * data.avgRating + rating.rating) /
  //         (data.numRatings + 1);

  //     transaction.update(document, {
  //       numRatings: data.numRatings + 1,
  //       avgRating: newAverage
  //     });
  //     return transaction.set(newRatingDocument, rating);
  //   });
  // });

  //TODO: continue here
  try{
          let response = await fetch(`${ratings_api}/add`, 
                      { method: "POST",
                        mode: "no-cors",
                        headers: {
                          'Content-Type': 'application/json' 
                        },
                        body: JSON.stringify(
                          { id: restaurantID, 
                            r: rating 
                          })
                      })
          let data = await response.json();
          console.log("adding a new ratings", data);
          return data
        }
  catch(err){
    console.log(err)
  }

  
// that.addRating(id, {
//   rating: rating,
//   text: dialog.querySelector('#text').value,
//   userName: 'Anonymous (Web)',
//   timestamp: new Date(),
//   userId: "Anonymous"
// })

};
