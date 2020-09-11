//
//  File.swift
//  CraigslistApp
//
//  Created by Eric Nguyen on 9/10/20.
//  Copyright © 2020 Eric Nguyen. All rights reserved.
//

import Foundation
import Alamofire

class APIHandler {
    static func addURL(hyperlink: String, craigslist_id:Int, keywords: Int, date: String){
        print("Request Processing")
        let parameters: Parameters = ["hyperlink": hyperlink, "craigslist_id": craigslist_id, "keywords": keywords, "date": date]

        AF.request("http://127.0.0.1:5000/Url", method: .post, parameters: parameters).responseJSON { response in
            debugPrint(response)
        }
        
    }
    
    static func addSearch(keywords: String, min_price: Int, max_price: Int){
        print("Request Processing")
        let parameters: Parameters = ["keywords": keywords, "min_price": min_price, "max_price": max_price]

        AF.request("http://127.0.0.1:5000/Search", method: .post, parameters: parameters).responseJSON { response in
            debugPrint(response)
        }
        
    }
}
