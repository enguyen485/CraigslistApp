//
//  TableViewController.swift
//  CraigslistApp
//
//  Created by Eric Nguyen on 9/11/20.
//  Copyright © 2020 Eric Nguyen. All rights reserved.
//

import UIKit


class DetectorController: UITableViewController {
    
    var detectors = [(id: Int, keywords: String, min_price: Int, max_price: Int)]()
    var id = 0
    var contact: Int?
    override func viewDidLoad() {
        super.viewDidLoad()

        APIHandler.getDetectors{ [weak self] (detectors) in
            self?.detectors = detectors
            self?.tableView.reloadData()
        }
        
           
    }

    // MARK: - Table view data source
   
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        id = detectors[indexPath[1]].id
    }
    
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // #warning Incomplete implementation, return the number of rows
        return detectors.count
        
    }
    
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
   
        let cell = tableView.dequeueReusableCell(withIdentifier: "DetectorItem", for: indexPath)

        cell.textLabel!.text = detectors[indexPath[1]].keywords
        cell.detailTextLabel!.text = "Minimum Price: " + String(detectors[indexPath[1]].min_price) + ", Maximum price: " + String(detectors[indexPath[1]].max_price)
        
        return cell
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        guard let UrlController = segue.destination as? UrlController,
            let index = tableView.indexPathForSelectedRow?.row
            else{
                return
        }
        UrlController.contact = detectors[index].id
    }
    

}
