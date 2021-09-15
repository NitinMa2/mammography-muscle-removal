import axios from "axios";

const url = "/api/segmentation";

// class to help with api calls to segmentation algorithm
class SegmentationService {
    // Get
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

    // Post
    static postDocument(data) {
        return axios.post(url, {
            data,
        });
    }
}

export default SegmentationService;
