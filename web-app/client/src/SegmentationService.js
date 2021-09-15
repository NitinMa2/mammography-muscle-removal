import axios from "axios";

const url = "/api/segmentation";

class SegmentationService {
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

    static postDocument(data) {
        return axios.post(url, {
            data,
        });
    }
}

export default SegmentationService;
