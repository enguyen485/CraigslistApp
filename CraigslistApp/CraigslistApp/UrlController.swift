//
//  UrlController.swift
//  CraigslistApp
//
//  Created by Eric Nguyen on 9/12/20.
//  Copyright © 2020 Eric Nguyen. All rights reserved.
//

import UIKit

class UrlController: UITableViewController {
    
    var contact: Int?
    var urls = [(String)]()
    override func viewDidLoad() {
        super.viewDidLoad()

        
        APIHandler.getUrls(keywords: contact! + 1){ [weak self] (urls) in
            self?.urls = urls
            self?.tableView.reloadData()
            print(urls)
        }
        
    }

    // MARK: - Table view data source


    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // #warning Incomplete implementation, return the number of rows
        return urls.count
    }

    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "UrlItem", for: indexPath)
        cell.textLabel!.text = urls[indexPath[1]]
        // Configure the cell...

        return cell
    }
    


}
