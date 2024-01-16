package me.redraskaldoesgaming.MineplexGadgets;

import java.util.ArrayList;

import org.bukkit.Bukkit;
import org.bukkit.ChatColor;
import org.bukkit.Material;
import org.bukkit.enchantments.Enchantment;
import org.bukkit.entity.Player;
import org.bukkit.inventory.Inventory;
import org.bukkit.inventory.ItemStack;
import org.bukkit.inventory.meta.ItemMeta;

public class Menu {

	public static Inventory myInventory = Bukkit.createInventory(null, 54, "Gadgets");
	// The first parameter, is the inventory owner. I make it null to let everyone use it.
	//The second parameter, is the slots in a inventory. Must be a multiple of 9. Can be up to 54.
	//The third parameter, is the inventory name. This will accept chat colors.
	
	static {
		createDisplay(Material.BED, 1, false, myInventory, 4, ChatColor.GRAY + "Close", "");
		createDisplay(Material.ENDER_PEARL, 1, true, myInventory, 19, ChatColor.GREEN + "" + ChatColor.BOLD + "Activate Ethereal Pearl", ChatColor.WHITE + "Take a ride through the skies with your very own Ethereal Pearl!");
		createDisplay(Material.FIREWORK, 1, false, myInventory, 20, ChatColor.GREEN + "" + ChatColor.BOLD + "Activate Fireworks", ChatColor.WHITE + "Need to celebrate?! Use some fireworks! Pew pew pew!");
		createDisplay(Material.TNT, 1, false, myInventory, 21, ChatColor.GREEN + "" + ChatColor.BOLD + "Activate TNT", ChatColor.WHITE + "Blow some people up! KABOOM!");
		createDisplay(Material.MELON_BLOCK, 1, false, myInventory, 22, ChatColor.GREEN + "" + ChatColor.BOLD + "Activate Melon Launcher", ChatColor.WHITE + "Deliciously fun! Eat the melon slices for a temporary speed boost!");
		createDisplay(Material.TRIPWIRE_HOOK, 1, false, myInventory, 23, ChatColor.GREEN + "" + ChatColor.BOLD + "Activate Flesh Hook", ChatColor.WHITE + "Make new friends by throwing a hook into their face and pulling them towards you!");
		createDisplay(Material.GOLD_BARDING, 1, false, myInventory, 24, ChatColor.GREEN + "" + ChatColor.BOLD + "Activate Paintball Gun", ChatColor.WHITE + "PEW PEW PEW PEW!");
		createDisplay(Material.IRON_BARDING, 1, false, myInventory, 25, ChatColor.GREEN + "" + ChatColor.BOLD + "Activate Bat Blaster", ChatColor.WHITE + "Launch waves of annoying bats at people you don't like!");
		createDisplay(Material.YELLOW_FLOWER, 1, false, myInventory, 28, ChatColor.GREEN + "" + ChatColor.BOLD + "Activate Coin Party Bomb", ChatColor.WHITE + "It's party time! you will be everyones favourite player when you use one of these!");
		createDisplay(Material.INK_SACK, 1, false, myInventory, 49, ChatColor.GRAY + "Clear Gadget", "");
		//The first parameter, is the slot that is assigned to. Starts counting at 0
		}
	
	public static void createDisplay(Material material, int amount, boolean isEnchanted, Inventory inv, int Slot, String name, String lore) {
		ItemStack item = new ItemStack(material);
		ItemMeta meta = item.getItemMeta();
		meta.setDisplayName(name);
		item.setAmount(amount);
		ArrayList<String> Lore = new ArrayList<String>();
		Lore.add(lore);
		meta.setLore(Lore);
		if(isEnchanted) {
		meta.addEnchant(Enchantment.OXYGEN, 1, true);
		} else {
			//Do Nothing
		}
		item.setItemMeta(meta);
		 
		inv.setItem(Slot, item); 
		 
		}
	
	public static void openInventory(Player player) {
		player.openInventory(myInventory);
	}
	
	public static void getMenu() {
		return Menu();
	}
}
