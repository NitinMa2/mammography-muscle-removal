import axios from "axios";

const url = "/api/segmentation";

// class to help with api calls to segmentation algorithm
class SegmentationService {
    /*
    ------------ REFERENCE CODE ------------

    //Get
    static getDocuments() {
        return new Promise(async (resolve, reject) => {
            try {
                const res = await axios.get(url);
                const data = res.data;
                resolve(data);
            } catch (err) {
                reject(err);
            }
        });
    }

    //Post
    static postDocument(data) {
        return axios.post(url, {
            data,
        });
    }

    ----------------------------------------
    */

    static async postMammogram(base64Image) {
        // makes an API request to the backend
        return new Promise(async (resolve, reject) => {
            try {
                // post the image and get a response
                const res = await axios.post(url, {
                    base64Image,
                });
                // pass the result to the caller
                const data = res.data.segmentedImage;
                resolve(data);
            } catch (err) {
                // error with the API call
                reject(err);
            }
        });
    }
}

export default SegmentationService;
