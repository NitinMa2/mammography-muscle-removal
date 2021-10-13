import axios from "axios";

const url = "/api/rating";

// class to help with storing the user rating in MongoDB
class RatingService {
    //Post
    static async postRating(ratingIsGood) {
        // makes an API request to the backend
        return new Promise(async (resolve, reject) => {
            try {
                // post the rating
                await axios.post(url, {
                    ratingIsGood,
                });
                resolve();
            } catch (err) {
                // error with the API call
                reject(err);
            }
        });
    }
}

export default RatingService;
